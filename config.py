import os
from dotenv import load_dotenv

load_dotenv()


def _as_bool(value: str, default: bool) -> bool:
    """'true/1/yes/on' → True, 'false/0/no/off' → False, 미설정 → default."""
    v = (value or "").strip().lower()
    if not v:
        return default
    return v in ("1", "true", "yes", "y", "on")


# ── 사방넷 API 호스트 (기본값: 운영) ─────────────────────────
# 사방넷 연동 개발자센터(https://developer.sabangnet.co.kr) 기준 호스트
#   운영     : https://api.sabangnet.co.kr
#   샌드박스 : https://sandbox.sabangnet.co.kr
# ⚠️ 운영 호스트로 실행하면 상품 등록·발주 등 쓰기 API가 실데이터에 반영됩니다.
#    기능 확인 목적이라면 SABANGNET_API_SERVER 를 샌드박스로 지정하세요.
SABANGNET_API_SERVER = os.getenv(
    "SABANGNET_API_SERVER", "https://api.sabangnet.co.kr"
)
# 사방넷 API 경로 prefix (주문관리=/v3/sb, 창고관리=/v3/sbf)
# ※ OpenAPI 명세상의 /gw/v3 는 게이트웨이 내부 경로이며 외부 호출 시 GW_ROUTE_001(404)이 반환됩니다.
SABANGNET_API_BASE = os.getenv(
    "SABANGNET_API_BASE", f"{SABANGNET_API_SERVER}/v3/sb"
)

# ── OAuth2 토큰 발급 ─────────────────────────────────────────
TOKEN_URL = os.getenv(
    "TOKEN_URL", f"{SABANGNET_API_SERVER}/oauth2/token"
)

# ── 앱 Client 정보 (개발자센터 > 앱 관리 > 앱 상세) ──────────
# 자격증명은 코드에 두지 않습니다. .env 에만 입력하세요 (.env 는 커밋 금지).
CLIENT_ID = os.getenv("CLIENT_ID", "")
# bcrypt salt로 사용하는 SecretKey
SECRET_KEY = os.getenv("SECRET_KEY", "")
CLIENT_TYPE = os.getenv("CLIENT_TYPE", "SB_APP")

# ── 서비스 계정 ID (API 요청 헤더 X-Svc-Acnt-Id) ─────────────
# 호출 대상 고객사의 서비스코드. 누락 시 게이트웨이가 GW_REQ_002(400)를 반환합니다.
SVC_ACNT_ID = os.getenv("SVC_ACNT_ID", "")

# ── 직접 Bearer Token 지정 (설정 시 토큰 발급 과정 생략) ───────
BEARER_TOKEN = os.getenv("BEARER_TOKEN", "")

# ── 풀필먼트(창고관리) API ────────────────────────────────────
# 개발자센터 가이드 기준: 창고관리 API는 주문관리와 동일 호스트를 공유하며
# 경로 접두사 /v3/sbf/** 로 구분됩니다. (주문관리=/v3/sb, 창고관리=/v3/sbf)
FULFILLMENT_API_BASE = os.getenv(
    "FULFILLMENT_API_BASE", f"{SABANGNET_API_SERVER}/v3/sbf"
)

TIMEOUT = 30
# 운영·샌드박스 게이트웨이는 TLS 1.3 핸드셰이크에서 사내 CA 서명 인증서를 제시하므로
# requests(OpenSSL) 기본 신뢰 저장소로는 검증에 실패합니다. (TLS 1.2 에서는 공인 인증서)
# 사내 CA를 신뢰하도록 구성했다면 VERIFY_SSL=true 로 올리세요.
VERIFY_SSL = _as_bool(os.getenv("VERIFY_SSL", ""), False)
