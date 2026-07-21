"""사방넷 풀필먼트 API 검증용 더미 데이터 (sbf-sample.csv mw821787 기준)."""

# ──────────────────────────────────────────────────────────────
# 1. 재고
# ──────────────────────────────────────────────────────────────

# #1 재고조회(단일) — GET /v3/sbf/inventory/stock/{id}
STOCK_GET_PATH_PARAM = 10

# #2 재고조회(벌크) — GET /v3/sbf/inventory/stocks
STOCK_LIST_PARAMS = {
    "shipping_product_ids": "10,20",
    "page": 1,
}

# #3 유통기한별 재고조회(벌크) — GET /v3/sbf/inventory/stock_expire
STOCK_EXPIRE_PARAMS = {
    "shipping_product_ids": [11, 10],
    "page": 1,
}

# #4 로케이션 재고조회(다중상품) — GET /v3/sbf/inventory/stock/locations
STOCK_LOCATION_BULK_PARAMS = {
    "loc_type": 2,
    "location_id": 2,
    "shipping_product_ids": [1, 3],
}

# ──────────────────────────────────────────────────────────────
# 2. 입고
# ──────────────────────────────────────────────────────────────

# #5 입고예정 등록(단일) — POST /v3/sbf/inventory/receiving_plan
RECEIVING_PLAN_CREATE_BODY = {
    "receiving_plan_code": "260518-03",
    "plan_date": "20260511",
    "memo": "입고-5/11",
    "add_info1": "5/8",
    "add_info2": "입고2",
    "add_info3": "info3",
    "add_info4": "",
    "add_info5": "",
    "plan_product_list": [
        {
            "shipping_product_id": 3,
            "quantity": 100,
            "expire_date": "20301211",
            "make_date": "20260508",
        },
        {
            "shipping_product_id": 15,
            "quantity": 20,
        },
    ],
}

# #6 입고예정 조회(벌크) — GET /v3/sbf/inventory/receiving_plans
RECEIVING_PLAN_LIST_PARAMS = {
    "receiving_plan_code": "260518-03",
    "plan_date": "20260511",
    "plan_status": 1,
    "page": 1,
}

# #7 예정대비입고현황 조회(단일) — GET /v3/sbf/inventory/receiving_plan_result/{id}
RECEIVING_PLAN_RESULT_PATH_PARAM = 16

# #8 입고작업내역 조회(벌크) — GET /v3/sbf/inventory/receiving_works
RECEIVING_WORK_LIST_PARAMS = {
    "start_dt": "20260506",
    "end_dt": "20260506",
    "receiving_plan_id": 15,
    "receiving_type": 1,
    "work_type": 1,
    "shipping_product_ids": [15, 2],
}

# ──────────────────────────────────────────────────────────────
# 3. 출고
# ──────────────────────────────────────────────────────────────

# #9 출고 조회(벌크) — GET /v3/sbf/releases
RELEASE_LIST_PARAMS = {
    "release_ids": 14,
    "release_codes": "R20260506-00001",
    "order_ids": 14,
    "shipping_order_info_id": 6,
    "release_date": "20260506",
    "request_shipping_dt": "20260506",
    "start_complete_dt": "20260506",
    "end_complete_dt": "20260506",
    "page": 1,
}

# #10 출고대상상품 조회(벌크) — GET /v3/sbf/release/items
RELEASE_ITEM_LIST_PARAMS = {
    "shipping_order_info_id": 9,
    "release_ids": 18,
    "release_codes": ["R2026050600004", "R20260506-00005"],
}

# #11 출고대상상품재고할당 조회(벌크) — GET /v3/sbf/release/item_stocks
RELEASE_ITEM_STOCK_LIST_PARAMS = {
    "shipping_order_info_id": 11,
    "release_codes": "R20260506-00007",
    "release_ids": 20,
}

# #12 출고회차 조회 — GET /v3/sbf/release/shipping_work
RELEASE_SHIPPING_WORK_LIST_PARAMS = {
    "order_date": "20260506",
    "page": 1,
}

# #13 운송장 일반 조회(벌크) — GET /v3/sbf/release/shipping_codes
SHIPPING_CODE_LIST_PARAMS = {
    "request_shipping_dt": "20260506",
    "company_order_code": "A-20260430",
    "order_id": 14,
    "release_id": 14,
    "delivery_agency_id": 2,
    "release_status": 7,
    "page": 1,
}

# ──────────────────────────────────────────────────────────────
# 4. 반품
# ──────────────────────────────────────────────────────────────

# #14 반품 조회(벌크) — GET /v3/sbf/release_return/searchs
RETURN_LIST_PARAMS = {
    "start_request_dt": "20260502",
    "end_request_dt": "20260530",
    "start_complete_dt": "20260502",
    "end_complete_dt": "20260530",
    "release_return_info_ids": [7, 8, 9, 10],
    "return_status": 5,
    "page": 1,
}

# ──────────────────────────────────────────────────────────────
# 5. 발주
# ──────────────────────────────────────────────────────────────

# #15 발주 등록(단일) — POST /v3/sbf/request/order
ORDER_CREATE_BODY = {
    "company_order_code": "A-20260507",
    "shipping_method_id": 1,
    "request_shipping_dt": "20260520",
    "buyer_name": "고길동",
    "receiver_name": "김민수",
    "tel1": "010-2525-3636",
    "tel2": "0246348620",
    "zipcode": "07788",
    "shipping_address1": "서울시 강서구 공항대로 168",
    "shipping_address2": "407호",
    "shipping_message": "안전 배송",
    "channel_id": 3,
    "memo1": "관리메모1",
    "memo2": "관리메모2",
    "memo3": "관리메모3",
    "memo4": "관리메모4",
    "memo5": "관리메모5",
    "order_item_list": [
        {
            "sales_product_id": 37,
            "quantity": 1,
            "item_cd1": "현대-그랜저",
            "item_cd2": "상품메모2",
            "item_cd3": "상품메모3",
        },
        {
            "sales_product_id": 36,
            "quantity": 1,
            "item_cd1": "현대-소나타",
            "item_cd2": "상품메모21",
            "item_cd3": "상품메모31",
        },
    ],
}

# #16 발주 등록(벌크) — POST /v3/sbf/request/orders
ORDER_BULK_CREATE_BODY = {
    "request_data_list": [
        {
            "company_order_code": "A-20260507-4",
            "shipping_method_id": 1,
            "request_shipping_dt": "20260520",
            "buyer_name": "아워홈",
            "receiver_name": "참좋은",
            "tel1": "010-2525-3636",
            "tel2": "0246348620",
            "zipcode": "07788",
            "shipping_address1": "서울시 강서구 공항대로 168",
            "shipping_address2": "407호",
            "shipping_message": "안전 배송",
            "channel_id": 3,
            "memo1": "관리메모1",
            "memo2": "관리메모2",
            "memo3": "관리메모3",
            "memo4": "관리메모4",
            "memo5": "관리메모5",
            "order_item_list": [
                {
                    "sales_product_id": 37,
                    "quantity": 1,
                    "item_cd1": "현대-그랜저",
                    "item_cd2": "상품메모2",
                    "item_cd3": "상품메모3",
                },
                {
                    "sales_product_id": 36,
                    "quantity": 1,
                    "item_cd1": "현대-소나타",
                    "item_cd2": "상품메모21",
                    "item_cd3": "상품메모31",
                },
            ],
        },
        {
            "company_order_code": "A-20260507-5",
            "shipping_method_id": 1,
            "request_shipping_dt": "20260520",
            "buyer_name": "김수로",
            "receiver_name": "인터넷",
            "tel1": "010-4589-2888",
            "tel2": "0246348620",
            "zipcode": "07788",
            "shipping_address1": "서울시 강서구 공항대로 168",
            "shipping_address2": "301호",
            "shipping_message": "안전 배송",
            "channel_id": 3,
            "memo1": "관리메모1",
            "memo2": "관리메모2",
            "memo3": "관리메모3",
            "memo4": "관리메모4",
            "memo5": "관리메모5",
            "order_item_list": [
                {
                    "sales_product_id": 47,
                    "quantity": 2,
                    "item_cd1": "기아-K9",
                    "item_cd2": "상품2",
                    "item_cd3": "상품3",
                },
                {
                    "sales_product_id": 50,
                    "quantity": 3,
                    "item_cd1": "기아-스포티지",
                    "item_cd2": "스포501",
                    "item_cd3": "스포503",
                },
            ],
        },
    ],
}

# #17 발주 조회(벌크) — GET /v3/sbf/request/orders
ORDER_LIST_PARAMS = {
    "order_code": "O20260506-00012",
    "company_order_codes": "A-20260430",
    "shipping_method_id": 1,
    "order_status": 7,
    "order_dt": "20260506",
    "request_shipping_dt": "20260506",
    "channel_id": 2,
    "page": 1,
}

# ──────────────────────────────────────────────────────────────
# 6. 상품
# ──────────────────────────────────────────────────────────────

# #18 출고상품 조회(벌크) — GET /v3/sbf/product/shipping_products
SHIPPING_PRODUCT_LIST_PARAMS = {
    "product_code": "FR-106",
    "product_name": "냉동",
    "category_id": 2,
    "status": 1,
    "page": 1,
}

# #19 판매상품 조회(벌크) — GET /v3/sbf/product/sales_products
SALES_PRODUCT_LIST_PARAMS = {
    "product_name": "냉동",
    "sales_product_code": "FR-106",
    "category_id": 3,
    "status": 1,
    "page": 1,
}

# ──────────────────────────────────────────────────────────────
# 7. 관리 (로케이션)
# ──────────────────────────────────────────────────────────────

# #20 로케이션 정보 조회(벌크) — GET /v3/sbf/locations
LOCATION_LIST_PARAMS = {
    "location_ids": [19, 20],
    "loc_type": 2,
    "page": 1,
}
