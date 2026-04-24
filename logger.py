import os
from datetime import datetime

_LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")

_success_file = None
_fail_file = None


def setup_logging():
    global _success_file, _fail_file
    os.makedirs(_LOG_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    success_path = os.path.join(_LOG_DIR, f"{ts}_success.log")
    fail_path = os.path.join(_LOG_DIR, f"{ts}_fail.log")
    _success_file = open(success_path, "w", encoding="utf-8")
    _fail_file = open(fail_path, "w", encoding="utf-8")
    print(f"[LOG] success → {success_path}")
    print(f"[LOG] fail    → {fail_path}")


def log_success(text: str):
    if _success_file:
        _success_file.write(text + "\n")
        _success_file.flush()


def log_fail(text: str):
    if _fail_file:
        _fail_file.write(text + "\n")
        _fail_file.flush()
