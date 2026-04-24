"""
사방넷 풀필먼트 API 검증 테스트 (20종)
─────────────────────────────────────────────────────────────────────────
 카테고리 | API명                        | 메서드 | 엔드포인트
─────────────────────────────────────────────────────────────────────────
 상품     | 출고상품 조회(벌크)            | GET    | /v3/product/shipping_products
 상품     | 판매상품 조회(벌크)            | GET    | /v3/product/sales_products
 재고     | 재고조회(단일)                 | GET    | /v3/inventory/stock/{shipping_product_id}
 재고     | 재고조회(벌크)                 | GET    | /v3/inventory/stocks
 재고     | 로케이션 재고조회(다중상품)     | POST   | /v3/inventory/stock/locations
 재고     | 유통기한별 재고조회             | GET    | /v3/inventory/stock_expire
 입고     | 입고예정 등록(단일)             | POST   | /v3/inventory/receiving_plan
 입고     | 입고예정 조회(벌크)             | GET    | /v3/inventory/receiving_plans
 입고     | 예정대비입고현황 조회           | GET    | /v3/inventory/receiving_plan_result/{id}
 입고     | 입고작업내역 조회(벌크)         | GET    | /v3/inventory/receiving_works
 발주     | 발주 등록(단일)                 | POST   | /v3/request/order
 발주     | 발주 등록(벌크)                 | POST   | /v3/request/orders
 발주     | 발주 조회(벌크)                 | GET    | /v3/request/orders
 출고     | 출고 조회(벌크)                 | GET    | /v3/releases
 출고     | 출고대상상품 조회(벌크)         | GET    | /v3/release/items
 출고     | 출고대상상품재고할당 조회(벌크) | GET    | /v3/release/item_stocks
 출고     | 출고회차 조회(벌크)             | GET    | /v3/release/shipping_work
 출고     | 운송장 일반 조회(벌크)          | GET    | /v3/release/shipping_codes
 반품     | 반품 조회(벌크)                 | GET    | /v3/release_return/searchs
 관리     | 로케이션 조회(벌크)             | GET    | /v3/locations
─────────────────────────────────────────────────────────────────────────

실행:
    # 환경변수 설정 (.env 파일 또는 직접 export)
    export FULFILLMENT_API_BASE=https://napi.sbfulfillment.co.kr/v3
    export BEARER_TOKEN=<발급된 풀필먼트 토큰>

    # 실행
    cd SB-DC/sample-code
    python fulfillment/test_fulfillment_api.py

    # 특정 테스트만
    python fulfillment/test_fulfillment_api.py --test stock_single
"""
import sys
import json
import argparse
import traceback
import requests

sys.path.insert(0, ".")
from config import FULFILLMENT_API_BASE, TIMEOUT, VERIFY_SSL
from auth import auth_headers
from logger import setup_logging, log_success, log_fail
from dummy_data.fulfillment_data import (
    SHIPPING_PRODUCT_LIST_PARAMS, SALES_PRODUCT_LIST_PARAMS,
    STOCK_GET_PATH_PARAM, STOCK_LIST_PARAMS,
    STOCK_LOCATION_BULK_BODY, STOCK_EXPIRE_PARAMS,
    RECEIVING_PLAN_CREATE_BODY, RECEIVING_PLAN_LIST_PARAMS,
    RECEIVING_PLAN_RESULT_PATH_PARAM, RECEIVING_WORK_LIST_PARAMS,
    ORDER_CREATE_BODY, ORDER_BULK_CREATE_BODY, ORDER_LIST_PARAMS,
    RELEASE_LIST_PARAMS, RELEASE_ITEM_LIST_PARAMS,
    RELEASE_ITEM_STOCK_LIST_PARAMS, RELEASE_SHIPPING_WORK_LIST_PARAMS,
    SHIPPING_CODE_LIST_PARAMS, RETURN_LIST_PARAMS, LOCATION_LIST_PARAMS,
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
# 1. 출고상품 조회(벌크)  GET /v3/product/shipping_products
# ─────────────────────────────────────────────────────────────
def test_shipping_product_list():
    url = f"{FULFILLMENT_API_BASE}/product/shipping_products"
    resp = requests.get(url, params=SHIPPING_PRODUCT_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("출고상품 조회(벌크)", resp, req_body=SHIPPING_PRODUCT_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 2. 판매상품 조회(벌크)  GET /v3/product/sales_products
# ─────────────────────────────────────────────────────────────
def test_sales_product_list():
    url = f"{FULFILLMENT_API_BASE}/product/sales_products"
    resp = requests.get(url, params=SALES_PRODUCT_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("판매상품 조회(벌크)", resp, req_body=SALES_PRODUCT_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 3. 재고조회(단일)  GET /v3/inventory/stock/{shipping_product_id}
# ─────────────────────────────────────────────────────────────
def test_stock_single():
    url = f"{FULFILLMENT_API_BASE}/inventory/stock/{STOCK_GET_PATH_PARAM}"
    resp = requests.get(url, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result(f"재고조회(단일) - product_id={STOCK_GET_PATH_PARAM}", resp)
    return resp


# ─────────────────────────────────────────────────────────────
# 4. 재고조회(벌크)  GET /v3/inventory/stocks
# ─────────────────────────────────────────────────────────────
def test_stock_list():
    url = f"{FULFILLMENT_API_BASE}/inventory/stocks"
    resp = requests.get(url, params=STOCK_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("재고조회(벌크)", resp, req_body=STOCK_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 5. 로케이션 재고조회(다중상품)  POST /v3/inventory/stock/locations
# ─────────────────────────────────────────────────────────────
def test_stock_location_bulk():
    url = f"{FULFILLMENT_API_BASE}/inventory/stock/locations"
    resp = requests.post(url, json=STOCK_LOCATION_BULK_BODY, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("로케이션 재고조회(다중상품)", resp, req_body=STOCK_LOCATION_BULK_BODY)
    return resp


# ─────────────────────────────────────────────────────────────
# 6. 유통기한별 재고조회  GET /v3/inventory/stock_expire
# ─────────────────────────────────────────────────────────────
def test_stock_expire():
    url = f"{FULFILLMENT_API_BASE}/inventory/stock_expire"
    resp = requests.get(url, params=STOCK_EXPIRE_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("유통기한별 재고조회", resp, req_body=STOCK_EXPIRE_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 7. 입고예정 등록(단일)  POST /v3/inventory/receiving_plan
# ─────────────────────────────────────────────────────────────
def test_receiving_plan_create():
    url = f"{FULFILLMENT_API_BASE}/inventory/receiving_plan"
    resp = requests.post(url, json=RECEIVING_PLAN_CREATE_BODY, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("입고예정 등록(단일)", resp, req_body=RECEIVING_PLAN_CREATE_BODY)
    return resp


# ─────────────────────────────────────────────────────────────
# 8. 입고예정 조회(벌크)  GET /v3/inventory/receiving_plans
# ─────────────────────────────────────────────────────────────
def test_receiving_plan_list():
    url = f"{FULFILLMENT_API_BASE}/inventory/receiving_plans"
    resp = requests.get(url, params=RECEIVING_PLAN_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("입고예정 조회(벌크)", resp, req_body=RECEIVING_PLAN_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 9. 예정대비입고현황 조회  GET /v3/inventory/receiving_plan_result/{id}
# ─────────────────────────────────────────────────────────────
def test_receiving_plan_result():
    url = f"{FULFILLMENT_API_BASE}/inventory/receiving_plan_result/{RECEIVING_PLAN_RESULT_PATH_PARAM}"
    resp = requests.get(url, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result(f"예정대비입고현황 조회 - plan_id={RECEIVING_PLAN_RESULT_PATH_PARAM}", resp)
    return resp


# ─────────────────────────────────────────────────────────────
# 10. 입고작업내역 조회(벌크)  GET /v3/inventory/receiving_works
# ─────────────────────────────────────────────────────────────
def test_receiving_work_list():
    url = f"{FULFILLMENT_API_BASE}/inventory/receiving_works"
    resp = requests.get(url, params=RECEIVING_WORK_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("입고작업내역 조회(벌크)", resp, req_body=RECEIVING_WORK_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 11. 발주 등록(단일)  POST /v3/request/order
# ─────────────────────────────────────────────────────────────
def test_order_create():
    url = f"{FULFILLMENT_API_BASE}/request/order"
    resp = requests.post(url, json=ORDER_CREATE_BODY, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("발주 등록(단일)", resp, req_body=ORDER_CREATE_BODY)
    return resp


# ─────────────────────────────────────────────────────────────
# 12. 발주 등록(벌크)  POST /v3/request/orders
# ─────────────────────────────────────────────────────────────
def test_order_bulk_create():
    url = f"{FULFILLMENT_API_BASE}/request/orders"
    resp = requests.post(url, json=ORDER_BULK_CREATE_BODY, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("발주 등록(벌크)", resp, req_body=ORDER_BULK_CREATE_BODY)
    return resp


# ─────────────────────────────────────────────────────────────
# 13. 발주 조회(벌크)  GET /v3/request/orders
# ─────────────────────────────────────────────────────────────
def test_order_list():
    url = f"{FULFILLMENT_API_BASE}/request/orders"
    resp = requests.get(url, params=ORDER_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("발주 조회(벌크)", resp, req_body=ORDER_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 14. 출고 조회(벌크)  GET /v3/releases
# ─────────────────────────────────────────────────────────────
def test_release_list():
    url = f"{FULFILLMENT_API_BASE}/releases"
    resp = requests.get(url, params=RELEASE_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("출고 조회(벌크)", resp, req_body=RELEASE_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 15. 출고대상상품 조회(벌크)  GET /v3/release/items
# ─────────────────────────────────────────────────────────────
def test_release_item_list():
    url = f"{FULFILLMENT_API_BASE}/release/items"
    resp = requests.get(url, params=RELEASE_ITEM_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("출고대상상품 조회(벌크)", resp, req_body=RELEASE_ITEM_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 16. 출고대상상품재고할당 조회(벌크)  GET /v3/release/item_stocks
# ─────────────────────────────────────────────────────────────
def test_release_item_stock_list():
    url = f"{FULFILLMENT_API_BASE}/release/item_stocks"
    resp = requests.get(url, params=RELEASE_ITEM_STOCK_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("출고대상상품재고할당 조회(벌크)", resp, req_body=RELEASE_ITEM_STOCK_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 17. 출고회차 조회(벌크)  GET /v3/release/shipping_work
# ─────────────────────────────────────────────────────────────
def test_release_shipping_work():
    url = f"{FULFILLMENT_API_BASE}/release/shipping_work"
    resp = requests.get(url, params=RELEASE_SHIPPING_WORK_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("출고회차 조회(벌크)", resp, req_body=RELEASE_SHIPPING_WORK_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 18. 운송장 일반 조회(벌크)  GET /v3/release/shipping_codes
# ─────────────────────────────────────────────────────────────
def test_shipping_code_list():
    url = f"{FULFILLMENT_API_BASE}/release/shipping_codes"
    resp = requests.get(url, params=SHIPPING_CODE_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("운송장 일반 조회(벌크)", resp, req_body=SHIPPING_CODE_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 19. 반품 조회(벌크)  GET /v3/release_return/searchs
# ─────────────────────────────────────────────────────────────
def test_return_list():
    url = f"{FULFILLMENT_API_BASE}/release_return/searchs"
    resp = requests.get(url, params=RETURN_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("반품 조회(벌크)", resp, req_body=RETURN_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 20. 로케이션 조회(벌크)  GET /v3/locations
# ─────────────────────────────────────────────────────────────
def test_location_list():
    url = f"{FULFILLMENT_API_BASE}/locations"
    resp = requests.get(url, params=LOCATION_LIST_PARAMS, headers=auth_headers(), timeout=TIMEOUT, verify=VERIFY_SSL)
    _print_result("로케이션 조회(벌크)", resp, req_body=LOCATION_LIST_PARAMS)
    return resp


# ─────────────────────────────────────────────────────────────
# 전체 실행
# ─────────────────────────────────────────────────────────────
ALL_TESTS = {
    # 상품
    "shipping_product_list":   test_shipping_product_list,
    "sales_product_list":      test_sales_product_list,
    # 재고
    "stock_single":            test_stock_single,
    "stock_list":              test_stock_list,
    "stock_location_bulk":     test_stock_location_bulk,
    "stock_expire":            test_stock_expire,
    # 입고
    "receiving_plan_create":   test_receiving_plan_create,
    "receiving_plan_list":     test_receiving_plan_list,
    "receiving_plan_result":   test_receiving_plan_result,
    "receiving_work_list":     test_receiving_work_list,
    # 발주
    "order_create":            test_order_create,
    "order_bulk_create":       test_order_bulk_create,
    "order_list":              test_order_list,
    # 출고
    "release_list":            test_release_list,
    "release_item_list":       test_release_item_list,
    "release_item_stock_list": test_release_item_stock_list,
    "release_shipping_work":   test_release_shipping_work,
    "shipping_code_list":      test_shipping_code_list,
    # 반품
    "return_list":             test_return_list,
    # 관리
    "location_list":           test_location_list,
}


def run_all():
    print("=" * 70)
    print("  창고관리(Fulfillment) 재고·입출고·반품 API 샘플 (20종)")
    print(f"  BASE URL: {FULFILLMENT_API_BASE}")
    print("=" * 70)

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

    print(f"\n{'=' * 70}")
    print(f"  결과: 성공 {passed} / 실패 {failed} / 전체 {passed + failed}")
    print("=" * 70)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="풀필먼트 API 검증 테스트")
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
