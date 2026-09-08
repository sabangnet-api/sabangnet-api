"""
사방넷 API 인증 토큰 발급 헬퍼

인증 흐름 (Client Credentials + bcrypt secretSign):
  1. timestamp = 현재시각(밀리초)
  2. data_to_sign = "{clientId}_{timestamp}"
  3. secretSign = base64(bcrypt.hashpw(data_to_sign, SECRET_KEY))
  4. POST /oauth2/token → access_token 획득
  5. 이후 API 요청: Authorization: Bearer {token} + X-Svc-Acnt-Id: {svcAcctId}

호스트: 운영 https://api.sabangnet.co.kr (개발자센터 https://developer.sabangnet.co.kr)
"""
import time
import base64
import bcrypt
import requests
import urllib3

from config import (
    TOKEN_URL, CLIENT_ID, SECRET_KEY, CLIENT_TYPE,
    SVC_ACNT_ID, BEARER_TOKEN, TIMEOUT, VERIFY_SSL,
)

if not VERIFY_SSL:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

_cached_token: str = ""


def get_token() -> str:
    """Bearer 토큰 반환 (캐싱 적용)."""
    global _cached_token
    if BEARER_TOKEN:
        return BEARER_TOKEN
    if _cached_token:
        return _cached_token
    _cached_token = _fetch_token()
    return _cached_token


def _validate_secret_key(key: str) -> None:
    """bcrypt salt 형식 검증. 실패 시 진단 메시지와 함께 ValueError 발생."""
    import re
    if not key:
        raise ValueError(
            "SECRET_KEY가 비어 있습니다\n"
            "  → 연동 개발자센터(https://developer.sabangnet.co.kr) > 앱 관리 > 앱 상세에서 발급받아 .env에 입력하세요"
        )
    # bcrypt salt: $2a$ 또는 $2b$ 또는 $2y$ + 2자리 cost + $ + 22자리 base64
    pattern = r'^\$2[aby]\$\d{2}\$.{22}$'
    if not re.match(pattern, key):
        hint = []
        if not key.startswith("$2"):
            hint.append("'$2a$', '$2b$', '$2y$' 중 하나로 시작해야 합니다")
        if len(key) != 29:
            hint.append(f"길이가 29자여야 하는데 현재 {len(key)}자입니다")
        raise ValueError(
            "SECRET_KEY 형식 오류\n"
            + ("\n".join(f"  → {h}" for h in hint) if hint else "  → bcrypt salt 형식($2a$NN$<22자>)이 아닙니다")
        )


def _fetch_token() -> str:
    """bcrypt secretSign 방식으로 OAuth2 토큰 발급."""
    if not CLIENT_ID:
        raise ValueError(
            "CLIENT_ID가 비어 있습니다\n"
            "  → 연동 개발자센터(https://developer.sabangnet.co.kr) > 앱 관리 > 앱 상세에서 발급받아 .env에 입력하세요"
        )
    _validate_secret_key(SECRET_KEY)
    timestamp = str(int(time.time() * 1000))
    data_to_sign = f"{CLIENT_ID}_{timestamp}".encode("utf-8")
    try:
        hashed = bcrypt.hashpw(data_to_sign, SECRET_KEY.encode("utf-8"))
    except ValueError as e:
        raise ValueError(
            f"bcrypt.hashpw 실패 — SECRET_KEY 형식을 확인하세요($2a$NN$<22자>)\n  원인: {e}"
        ) from e
    secret_sign = base64.b64encode(hashed).decode("utf-8")

    payload = {
        "grant_type": "client_credentials",
        "clientType": CLIENT_TYPE,
        "clientCd": CLIENT_ID,
        "timestamp": timestamp,
        "secretSign": secret_sign,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    resp = requests.post(TOKEN_URL, data=payload, headers=headers,
                         timeout=TIMEOUT, verify=VERIFY_SSL)
    if not resp.ok:
        safe_payload = {**payload, "secretSign": "***"}
        print(
            f"❌ 토큰 발급 실패 [{resp.status_code}] {TOKEN_URL}\n"
            f"  request payload : {safe_payload}\n"
            f"  response body   : {resp.text}"
        )
    resp.raise_for_status()
    token = resp.json().get("access_token", "")
    if not token:
        raise RuntimeError(f"토큰 발급 실패: {resp.text}")
    print(f"✅ 토큰 발급 성공")
    return token


def auth_headers() -> dict:
    """API 요청에 사용할 인증 헤더 반환."""
    if not SVC_ACNT_ID:
        raise ValueError(
            "SVC_ACNT_ID가 비어 있습니다 — 게이트웨이가 GW_REQ_002(400)를 반환합니다\n"
            "  → 개발자센터 > 앱 관리 > 앱 상세 > 사용 고객사의 서비스코드를 .env에 입력하세요"
        )
    return {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "X-Svc-Acnt-Id": SVC_ACNT_ID,
    }


def preflight() -> None:
    """실행 전 .env 자격증명 점검. 누락 시 요청을 보내지 않고 안내 후 종료."""
    missing = []
    if not BEARER_TOKEN:
        if not CLIENT_ID:
            missing.append("CLIENT_ID")
        if not SECRET_KEY:
            missing.append("SECRET_KEY")
    if not SVC_ACNT_ID:
        missing.append("SVC_ACNT_ID")
    if missing:
        raise SystemExit(
            "❌ .env 설정이 비어 있습니다: " + ", ".join(missing) + "\n"
            "  → cp .env.example .env 후, 연동 개발자센터(https://developer.sabangnet.co.kr)\n"
            "     > 앱 관리 > 앱 상세에서 발급받은 값을 입력하세요"
        )


def reset_token():
    """캐시된 토큰 초기화 (토큰 만료 시 재발급)."""
    global _cached_token
    _cached_token = ""
