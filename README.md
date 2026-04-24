# 사방넷 개발자센터 API 샘플 코드

사방넷 개발자센터에서 제공하는 두 가지 API를 Python으로 연동하는 샘플 코드입니다.

| 구분 | 설명 | API 수 |
|------|------|--------|
| **사방넷(Sabangnet) API** | 주문·상품·운송장·카테고리 등 쇼핑몰 관리 API | 14종 |
| **창고관리(Fulfillment) API** | 재고·입고·발주·출고·반품 등 풀필먼트 센터 연동 API | 20종 |

---

## 요구사항

- Python 3.8 이상
- 필수 패키지: `requests`, `python-dotenv`, `bcrypt`

---

## 빠른 시작

### 1. 패키지 설치

```bash
cd sample-code
pip install -r requirements.txt
```

### 2. 환경 설정

```bash
cp .env.example .env
```

`.env` 파일을 열어 아래 값을 입력합니다.

| 항목 | 설명 | 발급 위치 |
|------|------|-----------|
| `CLIENT_ID` | 앱 Client ID | 개발자센터 > 앱 관리 > 앱 상세 |
| `SECRET_KEY` | bcrypt 형식 SecretKey (`$2a$10$...` 형태) | 개발자센터 > 앱 관리 > 앱 상세 |
| `SVC_ACNT_ID` | 서비스 계정 ID | 개발자센터 > 서비스 계정 관리 |
| `CLIENT_TYPE` | 앱 유형 (`SB_APP` 고정) | — |

> **BEARER_TOKEN** 값을 직접 입력하면 토큰 발급 과정을 건너뜁니다. (선택 사항)

### 3. 실행

```bash
# 전체 실행 (사방넷 API + 창고관리 API)
python run_all.py

# 사방넷 API만 실행
python run_all.py --suite sabangnet

# 창고관리(풀필먼트) API만 실행
python run_all.py --suite fulfillment
```

---

## 개별 실행 및 단일 테스트

```bash
# 사방넷 API — 전체
python sabangnet/test_sabangnet_api.py

# 사방넷 API — 단일 테스트
python sabangnet/test_sabangnet_api.py --test product_get
python sabangnet/test_sabangnet_api.py --list        # 테스트 목록 확인

# 창고관리 API — 전체
python fulfillment/test_fulfillment_api.py

# 창고관리 API — 단일 테스트
python fulfillment/test_fulfillment_api.py --test stock_list
python fulfillment/test_fulfillment_api.py --list   # 테스트 목록 확인
```

---

## API 목록

### 사방넷(Sabangnet) API — 14종

| # | 카테고리 | API명 | 메서드 | 엔드포인트 |
|---|---------|-------|--------|-----------|
| 1 | 문의사항 | 문의사항 정보 조회 | GET | `/v3/sb/cs` |
| 2 | 문의사항 | 문의사항 답변 저장 | POST | `/v3/sb/cs/answer` |
| 3 | 상품 | 상품 조회 | GET | `/v3/sb/product` |
| 4 | 상품 | 상품 등록&수정 | POST | `/v3/sb/product/upsert` |
| 5 | 상품정보제공고시 | 목록 조회 | GET | `/v3/sb/product-info-notice/{noticeType}` |
| 6 | 쇼핑몰 | 쇼핑몰 정보 조회 | GET | `/v3/sb/mall/{shopDivCode}` |
| 7 | 운송장 | 운송장 저장/수정 | POST | `/v3/sb/waybill` |
| 8 | 주문 | 주문 목록 조회 | GET | `/v3/sb/order` |
| 9 | 추가상품 | 추가상품 등록&수정 | POST | `/v3/sb/additional-product` |
| 10 | 카테고리 | 전체 마이카테고리 목록 조회 | GET | `/v3/sb/category` |
| 11 | 카테고리 | 마이카테고리 등록&수정 | POST | `/v3/sb/category` |
| 12 | 카테고리 | 마이카테고리 목록 조회 | GET | `/v3/sb/category/{lCategoryCode}` |
| 13 | 클레임 | 클레임 목록 조회 | GET | `/v3/sb/claim` |
| 14 | 판매채널별상품 | 채널별 상품 등록&수정 | POST | `/v3/sb/channels-product` |

### 창고관리(Fulfillment) API — 20종

| # | 카테고리 | API명 | 메서드 | 엔드포인트 |
|---|---------|-------|--------|-----------|
| 1 | 상품 | 출고상품 조회(벌크) | GET | `/v3/product/shipping_products` |
| 2 | 상품 | 판매상품 조회(벌크) | GET | `/v3/product/sales_products` |
| 3 | 재고 | 재고조회(단일) | GET | `/v3/inventory/stock/{id}` |
| 4 | 재고 | 재고조회(벌크) | GET | `/v3/inventory/stocks` |
| 5 | 재고 | 로케이션 재고조회(다중상품) | POST | `/v3/inventory/stock/locations` |
| 6 | 재고 | 유통기한별 재고조회 | GET | `/v3/inventory/stock_expire` |
| 7 | 입고 | 입고예정 등록(단일) | POST | `/v3/inventory/receiving_plan` |
| 8 | 입고 | 입고예정 조회(벌크) | GET | `/v3/inventory/receiving_plans` |
| 9 | 입고 | 예정대비입고현황 조회 | GET | `/v3/inventory/receiving_plan_result/{id}` |
| 10 | 입고 | 입고작업내역 조회(벌크) | GET | `/v3/inventory/receiving_works` |
| 11 | 발주 | 발주 등록(단일) | POST | `/v3/request/order` |
| 12 | 발주 | 발주 등록(벌크) | POST | `/v3/request/orders` |
| 13 | 발주 | 발주 조회(벌크) | GET | `/v3/request/orders` |
| 14 | 출고 | 출고 조회(벌크) | GET | `/v3/releases` |
| 15 | 출고 | 출고대상상품 조회(벌크) | GET | `/v3/release/items` |
| 16 | 출고 | 출고대상상품재고할당 조회(벌크) | GET | `/v3/release/item_stocks` |
| 17 | 출고 | 출고회차 조회(벌크) | GET | `/v3/release/shipping_work` |
| 18 | 출고 | 운송장 일반 조회(벌크) | GET | `/v3/release/shipping_codes` |
| 19 | 반품 | 반품 조회(벌크) | GET | `/v3/release_return/searchs` |
| 20 | 관리 | 로케이션 조회(벌크) | GET | `/v3/locations` |

---

## 더미 데이터 수정

요청 파라미터 및 바디 예시는 `dummy_data/` 에 있습니다. 실제 연동 시 본인 계정 값으로 교체하세요.

| 파일 | 교체 필요 항목 |
|------|--------------|
| `dummy_data/sabangnet_data.py` | `DATE_START`, `DATE_END` (조회 날짜 범위) |
| `dummy_data/fulfillment_data.py` | `MEMBER_ID`, `SHIPPING_PRODUCT_ID`, `SALES_PRODUCT_ID`, `RECEIVING_PLAN_ID` |

---

## 인증 방식

**Client Credentials + bcrypt secretSign** 방식을 사용합니다.

```
1. timestamp  = 현재시각(밀리초)
2. data       = "{CLIENT_ID}_{timestamp}"
3. secretSign = Base64( bcrypt.hashpw(data, SECRET_KEY) )
4. POST /oauth2/token  →  access_token 획득
5. API 요청 헤더: Authorization: Bearer {token}
                  X-Svc-Acnt-Id: {SVC_ACNT_ID}
```

상세 구현은 [`auth.py`](auth.py)를 참고하세요.

---

## 파일 구조

```
sample-code/
├── run_all.py                      # 전체 실행 진입점
├── auth.py                         # 인증 토큰 발급 헬퍼
├── config.py                       # 환경 변수 로딩
├── requirements.txt                # 필수 패키지
├── .env.example                    # 환경 변수 템플릿 (값 없음, 커밋됨)
├── .env                            # 실제 인증 정보 (커밋 금지)
├── sabangnet/
│   └── test_sabangnet_api.py       # 사방넷 API 샘플 14종
├── fulfillment/
│   └── test_fulfillment_api.py     # 창고관리(풀필먼트) API 샘플 20종
└── dummy_data/
    ├── sabangnet_data.py           # 사방넷 API 요청 예시 데이터
    └── fulfillment_data.py         # 창고관리 API 요청 예시 데이터
```

---

## 트러블슈팅

| 오류 | 원인 | 해결 |
|------|------|------|
| `401 Unauthorized` | CLIENT_ID 또는 SECRET_KEY 불일치 | 개발자센터에서 최신 값 재복사 후 `.env` 업데이트 |
| `AUTH_001` | CLIENT_ID가 등록되지 않음 | 개발자센터 앱 활성 상태 확인 |
| `AUTH_003` | secretSign 검증 실패 | SECRET_KEY 재확인 (`$2a$10$...` 29자 형식) |
| `AUTH_006` | 타임스탬프 만료 (5분 초과) | 시스템 시간 동기화 확인 (`date` 명령) |
| `SSLError: CERTIFICATE_VERIFY_FAILED` | Self-signed 인증서 | `.env`에 `VERIFY_SSL=false` 설정 |
| `ValueError: SECRET_KEY 형식 오류` | `.env.example` 기본값 그대로 사용 중 | `.env`에 실제 발급 값 입력 |
