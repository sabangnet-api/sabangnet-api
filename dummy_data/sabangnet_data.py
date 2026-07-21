"""사방넷 API 검증용 더미 데이터."""

# ── 공통 날짜 범위 ─────────────────────────────────────────────
DATE_START = "20260101000000"
DATE_END   = "20260421235959"
DATE_START_8 = "20260101"
DATE_END_8   = "20260421"

# ──────────────────────────────────────────────────────────────
# 1. 문의사항 (CS)
# ──────────────────────────────────────────────────────────────
CS_SEARCH_REQUEST = {
    "startDate": DATE_START,
    "endDate": DATE_END,
    "page": 1,
    "perPage": 100,
    "csStatus": "NEW_RECEIPT",   # NEW_RECEIPT | ANSWER_SAVED | ANSWER_SENT | FORCED_CONVERSION
}

CS_ANSWER_REQUEST = {
    "items": [
        {
            "csSrno": 51280395,
            "answerContent": "고객님, 문의하신 사항에 대해 안내드립니다. 해당 상품은 재고가 충분하며 3~5일 내 발송 가능합니다.",
        }
    ]
}

# ──────────────────────────────────────────────────────────────
# 2. 상품
# ──────────────────────────────────────────────────────────────
PRODUCT_GET_PARAMS = {
    "productCode": "12345678",
    # "customProductCode": "MALL-PRD-001",  # productCode 또는 customProductCode 중 하나 사용
}

PRODUCT_UPSERT_REQUEST = {
    "products": [
        {
            "customProductCode": "SAMPLE-PRD-001",
            "productName": "테스트 반팔티셔츠 (S/M/L)",
            "engProductName": "Test T-Shirt",
            "manufacturerName": "테스트제조사",
            "originName": "DOMESTIC",               # DOMESTIC | FOREIGN 등
            "originAreaName": "경기도",
            "consumerPrice": 25000,
            "sellingPrice": 19900,
            "costPrice": 8000,
            "deliveryCostCode": "FREE",              # FREE | COLLECT | PREPAY | COLLECT_PREPAY
            "taxCode": "TAXABLE",                   # TAXABLE | TAX_FREE | NON_TAXABLE
            "productDivisionCode": "PURCHASE",      # CONSIGN | MANUFACTURE | PURCHASE | DIRECT
            "productSupplyStatusCode": "IN_SUPPLY", # WAITING | IN_SUPPLY | PAUSE | OUT_OF_STOCK
            "productTargetCode": "UNISEX",          # MALE | FEMALE | UNISEX | JUNIOR | BOY | GIRL
            "myCategoryCodeL": "01",
            "myCategoryCodeM": "0101",
            "myCategoryCodeS": "010101",
            "productDetailDescription": "<p>고품질 면 100% 반팔티셔츠입니다.</p>",
            "brandName": "샘플브랜드",
            "modelName": "ST-2024-001",
            "productTag": "티셔츠,반팔,여름",
            "seasonCode": "SS",                     # SPRING | SUMMER | AUTUMN | WINTER | FW | SS | SF
            "salesRegionCode": "NATIONWIDE",        # NATIONWIDE | NATIONWIDE_EXCEPT_ISLANDS | CAPITAL_AREA
            "optionInfo": {
                "stockUseYn": "Y",
                "optionEditCode": "RESET",          # RESET: 전체 초기화 후 재등록
                "options": [
                    {
                        "optionName": "색상",
                        "optionDetailName": "화이트",
                        "abbreviationName": "WHT",
                        "additionalAmount": 0,
                        "stockQuantity": 50,
                        "safetyStockQuantity": 5,
                        "barcode": "8801234567890",
                        "optionSupplyStatusCode": "SALE",   # SALE | SOLD_OUT | NOT_USE
                    },
                    {
                        "optionName": "색상",
                        "optionDetailName": "블랙",
                        "abbreviationName": "BLK",
                        "additionalAmount": 0,
                        "stockQuantity": 30,
                        "safetyStockQuantity": 5,
                        "barcode": "8801234567891",
                        "optionSupplyStatusCode": "SALE",
                    },
                ],
            },
            "imageInfo": [
                {"imageSrno": "1", "imagePath": "https://example.com/images/tshirt_main.jpg"},
                {"imageSrno": "2", "imagePath": "https://example.com/images/tshirt_sub.jpg"},
            ],
        }
    ]
}

# ──────────────────────────────────────────────────────────────
# 3. 상품정보제공고시
# ──────────────────────────────────────────────────────────────
PRODUCT_INFO_NOTICE_PARAMS = {
    "noticeType": "WEAR",   # WEAR | SHOES | BAG | COSMETICS | PROCESSED_FOOD 등
}

# ──────────────────────────────────────────────────────────────
# 4. 쇼핑몰
# ──────────────────────────────────────────────────────────────
MALL_INFO_PARAMS = {
    "shopDivCode": "SHOP",  # CHOP(일반) | SHOP(제휴) | GLOBAL(해외)
}

# ──────────────────────────────────────────────────────────────
# 5. 운송장
# ──────────────────────────────────────────────────────────────
WAYBILL_SAVE_REQUEST = {
    "forceUpdateYn": "N",
    "waybillList": [
        {
            "sbOrderNo": "20240101-001",
            "deliveryCompanyCode": "CJGLS",     # CJ대한통운
            "wayBillNo": "123456789012",
            "hopeDeliveryDate": "",
        },
        {
            "sbOrderNo": "20240101-002",
            "deliveryCompanyCode": "HANJIN",    # 한진택배
            "wayBillNo": "987654321098",
            "hopeDeliveryDate": "",
        },
    ],
}

# ──────────────────────────────────────────────────────────────
# 6. 주문
# ──────────────────────────────────────────────────────────────
ORDER_SEARCH_REQUEST = {
    "startDate": DATE_START_8,          # string (yyyyMMdd 또는 yyyyMMddHHmmss)
    "endDate": DATE_END_8,              # string
    "dateSearchCondition": 1,           # 1: 주문일, 2: 수집일, 3: 발송처리일
    "page": 1,
    "perPage": 100,                     # 50 ~ 1000
    "updateOrderStsYn": "N",            # N: 상태변경 없음 | Y: 신규→주문확인으로 변경
    "orderStatusList": ["001", "002"],  # 001: 신규주문, 002: 주문확인
    "responseItems": [                  # 명세 응답 항목 코드표 기준
        "SB_ORD_NO", "SHOP_ORD_NO", "ORDER_STATUS", "RECEIVER_NM",
        "CM_PRD_NM", "CM_SKU_NM", "ORD_CNT", "CT_DELIVERY_COST",
    ],
}

# ──────────────────────────────────────────────────────────────
# 7. 추가상품
# ──────────────────────────────────────────────────────────────
ADDITIONAL_PRODUCT_REQUEST = {
    "productInfoList": [
        {
            "actionType": "I",              # I: 등록 | U: 수정
            "shopCode": "shop0001",
            "groupCode": "G001",
            "groupName": "소이캔들세트",
            "groupType": "G",               # G | M | null
            "salesType": "CONSIGNMENT",     # CONSIGNMENT | PURCHASE | ETC
            "deliveryType": "SELF_COMPANY", # SELF_COMPANY | OTHER_COMPANY
            "supplierId": "SUP001",         # 매입처ID (선택)
            "comment": "프리미엄 소이캔들 추가상품 그룹",
            "groupInfoList": [
                {
                    "sbPrdSkuCode": "100001-0001",
                    "addProductOptionName": "바닐라향 소이캔들",
                    "salesPrice": 15000,
                    # READY | SALE | TEMP_SOLD_OUT | SOLD_OUT | NOT_USE
                    "productSupplyStatusCode": "SALE",
                }
            ],
        }
    ]
}

# ──────────────────────────────────────────────────────────────
# 8. 카테고리
# ──────────────────────────────────────────────────────────────
CATEGORY_SAVE_REQUEST = {
    "categories": [
        {
            "category": [
                {"code": "01", "name": "의류/패션", "level": 1, "sortSrno": 1, "useYn": "Y", "comment": ""},
                {"code": "0101", "name": "상의", "level": 2, "sortSrno": 1, "useYn": "Y", "comment": ""},
                {"code": "010101", "name": "반팔티셔츠", "level": 3, "sortSrno": 1, "useYn": "Y", "comment": ""},
            ]
        }
    ]
}

CATEGORY_BY_CODE_PARAMS = {
    "lCategoryCode": "01",
}

# ──────────────────────────────────────────────────────────────
# 9. 클레임
# ──────────────────────────────────────────────────────────────
CLAIM_SEARCH_REQUEST = {
    "startDate": DATE_START_8,          # string (yyyyMMdd 또는 yyyyMMddHHmmss)
    "endDate": DATE_END_8,              # string
    "page": 1,
    "perPage": 100,                     # 50 ~ 500
    "responseItems": ["SB_ORD_NO", "SHOP_ORD_NO", "CLAIM_TEXT", "CLAIM_STS_DIV_CD"],
}

# ──────────────────────────────────────────────────────────────
# 10. 판매채널별 상품관리
# ──────────────────────────────────────────────────────────────
CHANNEL_PRODUCT_REQUEST = {
    "products": [
        {
            "customProductCode": "SAMPLE-PRD-001",
            "shopCode": "shop0001",
            "productName": "테스트 반팔티셔츠 (쇼핑몰노출명)",
            "productDetailDescription": "<p>상품 상세 설명입니다.</p>",
            "salePrice": 19900,
            "shopMallShippingPolicyId": "B0000001",
            "shopMallStockRate": 100,
            "productAttributeClassificationCode": "001",
        }
    ]
}

# ──────────────────────────────────────────────────────────────
# 11. 주문 상태변경 (order-status)
#     허용 전이/상태별 필수값은 명세 참고. 아래는 대표 전이 예시.
#     - CANCEL_RECEIPT: cancelReasonCode 필수 (C로 시작하는 사유코드)
#     - EXCHANGE/RETURN_RECEIPT: claimReasonCode 필수 (E/R로 시작)
#     - EXCHANGE/RETURN_COMPLETED: warehouseCode + 입고수량(가용+불용>=1) 필수
#     - DELIVERY_PENDING: desiredShipDate(yyyyMMdd) 필수
# ──────────────────────────────────────────────────────────────
ORDER_STATUS_CHANGE_REQUEST = {
    "orders": [
        {
            "sbOrderNo": "20260101000001",
            "targetStatusCode": "ORDER_CONFIRM",   # 신규주문 → 주문확인
        },
        {
            "sbOrderNo": "20260101000002",
            "targetStatusCode": "CANCEL_RECEIPT",   # 취소접수
            "cancelReasonCode": "C001",             # 취소접수 전이 시 필수
            "claimContent": "고객 변심으로 인한 취소",
        },
    ]
}

# ──────────────────────────────────────────────────────────────
# 12. 표준카테고리 조회 (standard-category)
# ──────────────────────────────────────────────────────────────
STANDARD_CATEGORY_PARAMS = {
    # 대분류 enum(미지정 시 전체): FURNITURE_INTERIOR | BOOKS | DIGITAL_APPLIANCES |
    #   LIFE_HEALTH | SPORTS_LEISURE | FOOD | LEISURE_CONVENIENCE | BIRTH_PARENTING |
    #   FASHION_CLOTHES | FASHION_ACCESSORIES | BEAUTY
    "largeCategory": "FASHION_CLOTHES",
    "page": 1,
    "perPage": 100,
}

STANDARD_CATEGORY_BY_CODE_PARAMS = {
    "stdCategoryCode": "S001172",   # 표준카테고리코드
}
