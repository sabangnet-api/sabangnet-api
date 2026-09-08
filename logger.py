import os
from datetime import datetime

_LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")

_success_file = None
_fail_file = None


def _open_private(path: str):
    """소유자만 읽고 쓸 수 있는 권한(0600)으로 로그 파일 생성."""
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    return os.fdopen(fd, "w", encoding="utf-8")


def setup_logging():
    global _success_file, _fail_file
    os.makedirs(_LOG_DIR, mode=0o700, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    success_path = os.path.join(_LOG_DIR, f"{ts}_success.log")
    fail_path = os.path.join(_LOG_DIR, f"{ts}_fail.log")
    _success_file = _open_private(success_path)
    _fail_file = _open_private(fail_path)
    print(f"[LOG] success → {success_path}")
    print(f"[LOG] fail    → {fail_path}")
    print("[LOG] ⚠️ 로그에는 API 응답 전문(주문 수취인명·연락처·주소 등)이 그대로 기록됩니다.\n"
          "      외부 공유·이슈 첨부 전에 반드시 내용을 확인하고, 확인 후에는 삭제하세요.")


def log_success(text: str):
    if _success_file:
        _success_file.write(text + "\n")
        _success_file.flush()


def log_fail(text: str):
    if _fail_file:
        _fail_file.write(text + "\n")
        _fail_file.flush()
