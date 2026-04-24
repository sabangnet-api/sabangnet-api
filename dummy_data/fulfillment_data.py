"""사방넷 풀필먼트 API 검증용 더미 데이터."""

# ── 공통 상수 ─────────────────────────────────────────────────
MEMBER_ID = 70
SHIPPING_PRODUCT_ID = 43778   # 출고상품 ID (사전 등록 필요)
SALES_PRODUCT_ID = 54046      # 판매상품 ID
RECEIVING_PLAN_ID = 506       # 입고예정 ID

# ──────────────────────────────────────────────────────────────
# 1. 상품 조회 (출고상품 / 판매상품)
# ──────────────────────────────────────────────────────────────
SHIPPING_PRODUCT_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
}

SALES_PRODUCT_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
}

# ──────────────────────────────────────────────────────────────
# 2. 재고 조회
# ──────────────────────────────────────────────────────────────
STOCK_GET_PATH_PARAM = SHIPPING_PRODUCT_ID   # 단일: /v3/inventory/stock/{id}

STOCK_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
}

STOCK_LOCATION_BULK_BODY = {
    "member_id": MEMBER_ID,
    "shipping_product_id_list": [43778, 43779],
}

STOCK_EXPIRE_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "shipping_product_id": SHIPPING_PRODUCT_ID,
}

# ──────────────────────────────────────────────────────────────
# 3. 입고
# ──────────────────────────────────────────────────────────────
RECEIVING_PLAN_CREATE_BODY = {
    "member_id": MEMBER_ID,
    "receiving_plan_code": RECEIVING_PLAN_ID,
    "plan_date": 20260501,
    "memo": "테스트 입고예정 등록",
    "add_info1": "추가정보1",
    "add_info2": "",
    "add_info3": "",
    "add_info4": "",
    "add_info5": "",
    "plan_product_list": [
        {
            "shipping_product_id": SHIPPING_PRODUCT_ID,
            "quantity": 100,
            "expire_date": 20271231,
            "make_date": 20260401,
        }
    ],
}

RECEIVING_PLAN_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "start_dt": 20260101,
    "end_dt": 20261231,
}

RECEIVING_PLAN_RESULT_PATH_PARAM = RECEIVING_PLAN_ID   # /v3/inventory/receiving_plan_result/{id}

RECEIVING_WORK_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "start_dt": 20260101,
    "end_dt": 20261231,
}

# ──────────────────────────────────────────────────────────────
# 4. 발주
# ──────────────────────────────────────────────────────────────
ORDER_CREATE_BODY = {
    "member_id": MEMBER_ID,
    "company_order_code": "ORD-20260421-001",
    "shipping_method_id": 1,
    "request_shipping_dt": 20260425,
    "buyer_name": "홍길동",
    "receiver_name": "홍길동",
    "tel1": "010-1234-5678",
    "tel2": "",
    "zipcode": 12345,
    "shipping_address1": "서울시 강남구 테헤란로 152",
    "shipping_address2": "강남파이낸스센터 10층",
    "shipping_message": "문 앞에 놓아주세요",
    "channel_id": 1,
    "memo1": "테스트 발주",
    "memo2": "",
    "memo3": "",
    "order_product_list": [
        {
            "shipping_product_id": SHIPPING_PRODUCT_ID,
            "quantity": 2,
        }
    ],
}

ORDER_BULK_CREATE_BODY = {
    "member_id": MEMBER_ID,
    "order_list": [
        {
            "company_order_code": "ORD-20260421-002",
            "shipping_method_id": 1,
            "request_shipping_dt": 20260425,
            "buyer_name": "김철수",
            "receiver_name": "김철수",
            "tel1": "010-9876-5432",
            "tel2": "",
            "zipcode": 54321,
            "shipping_address1": "경기도 성남시 분당구 판교역로 235",
            "shipping_address2": "에이치스퀘어 S동",
            "shipping_message": "",
            "channel_id": 1,
            "memo1": "테스트 벌크 발주1",
            "order_product_list": [
                {"shipping_product_id": SHIPPING_PRODUCT_ID, "quantity": 1}
            ],
        }
    ],
}

ORDER_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "start_dt": 20260101,
    "end_dt": 20261231,
}

# ──────────────────────────────────────────────────────────────
# 5. 출고
# ──────────────────────────────────────────────────────────────
RELEASE_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "start_dt": 20260101,
    "end_dt": 20261231,
}

RELEASE_ITEM_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "start_dt": 20260101,
    "end_dt": 20261231,
}

RELEASE_ITEM_STOCK_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
}

RELEASE_SHIPPING_WORK_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "start_dt": 20260101,
    "end_dt": 20261231,
}

SHIPPING_CODE_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "start_dt": 20260101,
    "end_dt": 20261231,
}

# ──────────────────────────────────────────────────────────────
# 6. 반품
# ──────────────────────────────────────────────────────────────
RETURN_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
    "start_dt": 20260101,
    "end_dt": 20261231,
}

# ──────────────────────────────────────────────────────────────
# 7. 관리 (로케이션)
# ──────────────────────────────────────────────────────────────
LOCATION_LIST_PARAMS = {
    "page": 1,
    "page_size": 20,
    "member_id": MEMBER_ID,
}
