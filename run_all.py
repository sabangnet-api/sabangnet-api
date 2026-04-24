"""
사방넷 API + 풀필먼트 API 전체 검증 실행 (총 34종)

사용법:
    cd SB-DC/sample-code
    pip install -r requirements.txt

    # 환경변수 설정 예시 (.env 파일 사용 권장)
    cp .env.example .env
    # .env 파일을 열어 BEARER_TOKEN 등 값 입력

    # 전체 실행
    python run_all.py

    # 사방넷 API만
    python run_all.py --suite sabangnet

    # 풀필먼트 API만
    python run_all.py --suite fulfillment
"""
import sys
import argparse

sys.path.insert(0, ".")

from logger import setup_logging


def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="전체 API 검증 테스트 실행")
    parser.add_argument(
        "--suite",
        choices=["sabangnet", "fulfillment", "all"],
        default="all",
        help=(
            "실행할 API 스위트 선택 (기본값: all)\n"
            "  sabangnet  : 사방넷 주문·상품·운송장 관리 API (14종)\n"
            "  fulfillment: 창고관리(풀필먼트) 재고·입출고·반품 API (20종)\n"
            "  all        : 전체 실행"
        ),
    )
    args = parser.parse_args()

    if args.suite in ("sabangnet", "all"):
        from sabangnet.test_sabangnet_api import run_all as run_sb
        run_sb()

    if args.suite in ("fulfillment", "all"):
        from fulfillment.test_fulfillment_api import run_all as run_ff
        run_ff()


if __name__ == "__main__":
    main()
