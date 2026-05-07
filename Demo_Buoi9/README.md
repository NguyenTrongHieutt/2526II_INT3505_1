# Chiến lược nâng cấp API thanh toán từ v1 sang v2

## 1. Bối cảnh hệ thống

Hệ thống hiện tại đang cung cấp API thanh toán phiên bản v1:

```http
POST /api/v1/payments
```

Request v1:

```json
{
  "userId": 123,
  "amount": 500000,
  "paymentMethod": "BANKING"
}
```

Response v1:

```json
{
  "status": "success",
  "transactionId": "TXN123456"
}
```

## 2. Yêu cầu nâng cấp sang v2

Business muốn bổ sung:

- Hỗ trợ đa tiền tệ (VND, USD, EUR)
- Hỗ trợ nhiều phương thức thanh toán mới
- Chuẩn hóa response format
- Bổ sung metadata giao dịch
- Tăng bảo mật request

Breaking changes xuất hiện:

| Thay đổi                    | Loại         |
| --------------------------- | ------------ |
| userId → customerId         | Breaking     |
| paymentMethod đổi format    | Breaking     |
| Thêm currency               | Non-breaking |
| Response structure thay đổi | Breaking     |
| Thêm createdAt              | Non-breaking |

Vì có breaking changes nên cần tạo API version mới.

## 3. Chiến lược Versioning được chọn

Chọn URL Versioning:

- `/api/v1/payments`
- `/api/v2/payments`

### Vì sao chọn URL Versioning?

| Ưu điểm                     | Giải thích                            |
| --------------------------- | ------------------------------------- |
| Dễ hiểu                     | Developers nhìn URL biết ngay version |
| Dễ debug                    | Log và monitoring rõ ràng             |
| Tương thích frontend/mobile | Không cần custom header               |
| Phổ biến                    | Được dùng nhiều trong REST API        |

## 4. Thiết kế API v2

### Endpoint

```http
POST /api/v2/payments
```

### Request v2

```json
{
  "customerId": "CUS_001",
  "amount": 500000,
  "currency": "VND",
  "paymentMethod": {
    "type": "BANK_TRANSFER",
    "provider": "VCB"
  },
  "metadata": {
    "orderId": "ORD_1001"
  }
}
```

### Response v2

```json
{
  "success": true,
  "data": {
    "transactionId": "TXN999999",
    "amount": 500000,
    "currency": "VND",
    "status": "PROCESSING",
    "createdAt": "2026-05-07T10:00:00Z"
  }
}
```

## 5. So sánh v1 và v2

| Thành phần     | v1       | v2         |
| -------------- | -------- | ---------- |
| Customer field | userId   | customerId |
| Currency       | Không có | Có         |
| Payment method | String   | Object     |
| Response       | Đơn giản | Chuẩn hóa  |
| Metadata       | Không có | Có         |
| Timestamp      | Không có | Có         |

## 6. Kế hoạch Migration (Migration Plan)

### Giai đoạn 1 — Release v2

Deploy song song:

- `/api/v1/payments`
- `/api/v2/payments`

Cần cập nhật đầy đủ:

- Documentation
- SDK hỗ trợ cả v1 và v2

### Giai đoạn 2 — Deprecation Notice

Thông báo:

- v1 sẽ deprecated sau 3 tháng
- Khuyến khích migrate sang v2
- Gửi email + dashboard notification cho developers

### Giai đoạn 3 — Monitoring

Theo dõi:

- Tỷ lệ request v1/v2
- Error rate
- Client chưa migrate

Ví dụ metric:

| API Version | Traffic |
| ----------- | ------- |
| v1          | 35%     |
| v2          | 65%     |

### Giai đoạn 4 — Sunset v1

Sau deadline:

HTTP 410 Gone

Response:

```json
{
  "error": "API v1 has been retired. Please migrate to v2."
}
```

## 7. Chính sách Deprecation

### Header cảnh báo

```http
Deprecation: true
Sunset: Wed, 01 Oct 2026 00:00:00 GMT
```

### Warning response

```json
{
  "warning": "API v1 is deprecated and will be removed on 01 Oct 2026"
}
```

## 8. Thông báo Deprecation cho Developers

Dưới đây là mẫu thông báo có thể gửi cho developers.

Xin chào Developers,

Chúng tôi xin thông báo rằng Payment API v1 sẽ chính thức bị deprecated kể từ ngày 01/07/2026 và sẽ ngừng hoạt động hoàn toàn vào ngày 01/10/2026.

Phiên bản mới v2 đã được phát hành với các cải tiến:

- Hỗ trợ đa tiền tệ
- Chuẩn hóa response structure
- Bổ sung metadata giao dịch
- Cải thiện bảo mật và khả năng mở rộng

API mới:

```http
POST /api/v2/payments
```

Chúng tôi khuyến nghị các hệ thống hiện đang sử dụng v1 bắt đầu migrate sang v2 sớm nhất có thể.

Tài liệu migration:

- Mapping field từ v1 → v2
- Ví dụ request/response mới
- Hướng dẫn xử lý paymentMethod mới

Sau ngày 01/10/2026:

- API v1 sẽ trả về HTTP 410 Gone
- Mọi request tới v1 sẽ bị từ chối

Nếu cần hỗ trợ migration, vui lòng liên hệ team Platform/API.

Trân trọng,
Platform Engineering Team
