import os
from dotenv import load_dotenv

load_dotenv()

# ── 사방넷 API (Dev 환경) ─────────────────────────────────────
# 실제 Dev API 서버 (기존 python/product_regist.py 참고)
SABANGNET_API_SERVER = os.getenv(
    "SABANGNET_API_SERVER", "https://dev-api.fbsabangnet.co.kr"
)
# 사방넷 API 경로 prefix: 로컬=http://localhost:8080/gw/v3, Dev=/v3/sb
SABANGNET_API_BASE = os.getenv(
    "SABANGNET_API_BASE", f"{SABANGNET_API_SERVER}/v3/sb"
)

# ── OAuth2 토큰 발급 ─────────────────────────────────────────
TOKEN_URL = os.getenv(
    "TOKEN_URL", f"{SABANGNET_API_SERVER}/oauth2/token"
)

# ── 앱 Client 정보 (개발자센터 > 앱 관리) ───────────────────
# 기존 샘플코드(python/product_regist.py)에서 확인된 값
CLIENT_ID = os.getenv("CLIENT_ID", "ec3ddf5e-4743-46bd-9daf-b3816297133e")
# bcrypt salt로 사용하는 SecretKey
SECRET_KEY = os.getenv("SECRET_KEY", "$2a$10$defghijklmnopqrstuvwxy")
CLIENT_TYPE = os.getenv("CLIENT_TYPE", "SB_APP")

# ── 서비스 계정 ID (API 요청 헤더 X-Svc-Acnt-Id) ─────────────
SVC_ACNT_ID = os.getenv("SVC_ACNT_ID", "test_seller001")

# ── 직접 Bearer Token 지정 (설정 시 토큰 발급 과정 생략) ───────
BEARER_TOKEN = os.getenv("BEARER_TOKEN", "")

# ── 풀필먼트 API ──────────────────────────────────────────────
FULFILLMENT_API_BASE = os.getenv(
    "FULFILLMENT_API_BASE", "https://napi.sbfulfillment.co.kr/v3"
)

TIMEOUT = 30
VERIFY_SSL = os.getenv("VERIFY_SSL", "false").lower() != "false"
