"""
사방넷 API 검증 테스트 (14종)
─────────────────────────────────────────────────────────────────
 카테고리       | API명                  | 메서드 | 엔드포인트
─────────────────────────────────────────────────────────────────
 문의사항       | 문의사항 정보 조회       | GET    | /gw/v3/cs
 문의사항       | 문의사항 답변 저장       | POST   | /gw/v3/cs/answer
 상품           | 상품 조회               | GET    | /gw/v3/product
 상품           | 상품 등록&수정          | POST   | /gw/v3/product/upsert
 상품정보제공고시| 상품정보제공고시 목록 조회| GET   | /gw/v3/product-info-notice/{noticeType}
 쇼핑몰         | 쇼핑몰 정보 조회        | GET    | /gw/v3/mall/{shopDivCode}
 운송장         | 운송장 저장/수정        | POST   | /gw/v3/waybill
 주문           | 주문 목록 조회          | GET    | /gw/v3/order
 추가상품       | 추가상품 등록&수정       | POST   | /gw/v3/additional-product
 카테고리       | 전체 마이카테고리 목록 조회| GET  | /gw/v3/category
 카테고리       | 마이카테고리 등록&수정   | POST   | /gw/v3/category
 카테고리       | 마이카테고리 목록 조회   | GET    | /gw/v3/category/{lCategoryCode}
 클레임         | 클레임 목록 조회        | GET    | /gw/v3/claim
 판매채널별상품 | 채널별 상품 등록&수정   | POST   | /gw/v3/channels-product
─────────────────────────────────────────────────────────────────

실행:
    # 사전 준비
    pip install -r requirements.txt

    # 환경변수 설정 (.env 파일 또는 직접 export)
    export SABANGNET_GW_BASE=http://localhost:8080
    export BEARER_TOKEN=<발급된 토큰>

    # 실행
    cd SB-DC/sample-code
    python sabangnet/test_sabangnet_api.py

    # 특정 테스트만 실행
    python sabangnet/test_sabangnet_api.py --test cs_search
"""
import sys
import json
import argparse
import traceback
import requests

sys.path.insert(0, ".")
from config import SABANGNET_API_BASE, TIMEOUT, VERIFY_SSL
from auth import auth_headers
from logger import setup_logging, log_success, log_fail
from dummy_data.sabangnet_data import (
    CS_SEARCH_REQUEST, CS_ANSWER_REQUEST,
    PRODUCT_GET_PARAMS, PRODUCT_UPSERT_REQUEST,
    PRODUCT_INFO_NOTICE_PARAMS, MALL_INFO_PARAMS,
    WAYBILL_SAVE_REQUEST, ORDER_SEARCH_REQUEST,
    ADDITIONAL_PRODUCT_REQUEST, CATEGORY_SAVE_REQUEST,
    CATEGORY_BY_CODE_PARAMS, CLAIM_SEARCH_REQUEST,
    CHANNEL_PRODUCT_REQUEST,
)


# ─────────────────────────────────────────────────────────────
# 결과 출력 헬퍼
# ─────────────────────────────────────────────────────────────
def _print_result(name: str, resp: requests.Response, req_body=None, show_body: bool = True):
    status = resp.status_code
    ok = "✅" if status < 400 else "❌"
    lines = [f"\n{ok} [{status}] {name}", f"    URL: {resp.url}"]
    if show_body:
        if req_body is not None:
            lines.append(f"    REQUEST BODY: {json.dumps(req_body, ensure_ascii=False, indent=2)}")
        try:
            body = resp.json()
            lines.append(f"    RESPONSE BODY: {json.dumps(body, ensure_ascii=False, indent=2)}")
        except Exception:
            lines.append(f"    RESPONSE BODY: {resp.text}")
    output = "\n".join(lines)
    print(output)
    (log_success if status < 400 else log_fail)(output)


# ─────────────────────────────────────────────────────────────
# 1. 문의사항 정보 조회  GET /gw/v3/cs
# ─────────────────────────────────────────────────────────────
def test_cs_search():
    url = f"{SABANGNET_API_BASE}/cs"
    resp = requests.get(url, json=CS_SEARCH_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("문의사항 정보 조회", resp, req_body=CS_SEARCH_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 2. 문의사항 답변 저장  POST /gw/v3/cs/answer
# ─────────────────────────────────────────────────────────────
def test_cs_answer():
    url = f"{SABANGNET_API_BASE}/cs/answer"
    resp = requests.post(url, json=CS_ANSWER_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("문의사항 답변 저장", resp, req_body=CS_ANSWER_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 3. 상품 조회  GET /gw/v3/product
# ─────────────────────────────────────────────────────────────
def test_product_get():
    url = f"{SABANGNET_API_BASE}/product"
    resp = requests.get(url, params=PRODUCT_GET_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("상품 조회", resp, req_body=PRODUCT_GET_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 4. 상품 등록&수정  POST /gw/v3/product/upsert
# ─────────────────────────────────────────────────────────────
def test_product_upsert():
    url = f"{SABANGNET_API_BASE}/product/upsert"
    resp = requests.post(url, json=PRODUCT_UPSERT_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("상품 등록&수정", resp, req_body=PRODUCT_UPSERT_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 5. 상품정보제공고시 목록 조회  GET /gw/v3/product-info-notice/{noticeType}
# ─────────────────────────────────────────────────────────────
def test_product_info_notice():
    notice_type = PRODUCT_INFO_NOTICE_PARAMS["noticeType"]
    url = f"{SABANGNET_API_BASE}/product-info-notice/{notice_type}"
    resp = requests.get(url, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result(f"상품정보제공고시 목록 조회 ({notice_type})", resp)
    return resp


# ─────────────────────────────────────────────────────────────
# 6. 쇼핑몰 정보 조회  GET /gw/v3/mall/{shopDivCode}
# ─────────────────────────────────────────────────────────────
def test_mall_info():
    shop_div_code = MALL_INFO_PARAMS["shopDivCode"]
    url = f"{SABANGNET_API_BASE}/mall/{shop_div_code}"
    resp = requests.get(url, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result(f"쇼핑몰 정보 조회 ({shop_div_code})", resp)
    return resp


# ─────────────────────────────────────────────────────────────
# 7. 운송장 저장/수정  POST /gw/v3/waybill
# ─────────────────────────────────────────────────────────────
def test_waybill_save():
    url = f"{SABANGNET_API_BASE}/waybill"
    resp = requests.post(url, json=WAYBILL_SAVE_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("운송장 저장/수정", resp, req_body=WAYBILL_SAVE_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 8. 주문 목록 조회  GET /gw/v3/order
# ─────────────────────────────────────────────────────────────
def test_order_search():
    url = f"{SABANGNET_API_BASE}/order"
    resp = requests.get(url, json=ORDER_SEARCH_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("주문 목록 조회", resp, req_body=ORDER_SEARCH_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 9. 추가상품 등록&수정  POST /gw/v3/additional-product
# ─────────────────────────────────────────────────────────────
def test_additional_product():
    url = f"{SABANGNET_API_BASE}/additional-product"
    resp = requests.post(url, json=ADDITIONAL_PRODUCT_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("추가상품 등록&수정", resp, req_body=ADDITIONAL_PRODUCT_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 10. 전체 마이카테고리 목록 조회  GET /gw/v3/category
# ─────────────────────────────────────────────────────────────
def test_category_all():
    url = f"{SABANGNET_API_BASE}/category"
    resp = requests.get(url, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("전체 마이카테고리 목록 조회", resp)
    return resp


# ─────────────────────────────────────────────────────────────
# 11. 마이카테고리 등록&수정  POST /gw/v3/category
# ─────────────────────────────────────────────────────────────
def test_category_save():
    url = f"{SABANGNET_API_BASE}/category"
    resp = requests.post(url, json=CATEGORY_SAVE_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("마이카테고리 등록&수정", resp, req_body=CATEGORY_SAVE_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 12. 마이카테고리 목록 조회  GET /gw/v3/category/{lCategoryCode}
# ─────────────────────────────────────────────────────────────
def test_category_by_code():
    l_code = CATEGORY_BY_CODE_PARAMS["lCategoryCode"]
    url = f"{SABANGNET_API_BASE}/category/{l_code}"
    resp = requests.get(url, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result(f"마이카테고리 목록 조회 (대분류코드: {l_code})", resp)
    return resp


# ─────────────────────────────────────────────────────────────
# 13. 클레임 목록 조회  GET /gw/v3/claim
# ─────────────────────────────────────────────────────────────
def test_claim_search():
    url = f"{SABANGNET_API_BASE}/claim"
    resp = requests.get(url, json=CLAIM_SEARCH_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("클레임 목록 조회", resp, req_body=CLAIM_SEARCH_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 14. 채널별 상품 등록&수정  POST /gw/v3/channels-product
# ─────────────────────────────────────────────────────────────
def test_channel_product():
    url = f"{SABANGNET_API_BASE}/channels-product"
    resp = requests.post(url, json=CHANNEL_PRODUCT_REQUEST, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("채널별 상품 등록&수정", resp, req_body=CHANNEL_PRODUCT_REQUEST)
    return resp


# ─────────────────────────────────────────────────────────────
# 전체 실행
# ─────────────────────────────────────────────────────────────
ALL_TESTS = {
    "cs_search":         test_cs_search,
    "cs_answer":         test_cs_answer,
    "product_get":       test_product_get,
    "product_upsert":    test_product_upsert,
    "product_notice":    test_product_info_notice,
    "mall_info":         test_mall_info,
    "waybill_save":      test_waybill_save,
    "order_search":      test_order_search,
    "additional_product": test_additional_product,
    "category_all":      test_category_all,
    "category_save":     test_category_save,
    "category_by_code":  test_category_by_code,
    "claim_search":      test_claim_search,
    "channel_product":   test_channel_product,
}


def run_all():
    print("=" * 60)
    print("  사방넷(Sabangnet) 주문·상품 관리 API 샘플 (14종)")
    print(f"  BASE URL: {SABANGNET_API_BASE}")
    print("=" * 60)

    passed = failed = 0
    for name, fn in ALL_TESTS.items():
        try:
            resp = fn()
            if resp.status_code < 400:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"\n❌ [{name}] 예외 발생: {type(e).__name__}: {e}")
            print("    --- 스택 트레이스 ---")
            for line in traceback.format_exc().splitlines():
                print(f"    {line}")
            failed += 1

    print(f"\n{'=' * 60}")
    print(f"  결과: 성공 {passed} / 실패 {failed} / 전체 {passed + failed}")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="사방넷 API 검증 테스트")
    parser.add_argument("--test", help=f"단일 테스트 실행: {', '.join(ALL_TESTS.keys())}")
    parser.add_argument("--list", action="store_true", help="테스트 목록 출력")
    args = parser.parse_args()

    setup_logging()
    if args.list:
        print("사용 가능한 테스트:")
        for k in ALL_TESTS:
            print(f"  --test {k}")
    elif args.test:
        if args.test in ALL_TESTS:
            ALL_TESTS[args.test]()
        else:
            print(f"알 수 없는 테스트: {args.test}")
            sys.exit(1)
    else:
        run_all()
