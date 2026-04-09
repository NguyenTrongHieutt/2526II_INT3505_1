# Book Management API

## Giới thiệu

Thư mục này chứa tài liệu và cấu trúc thiết kế cho API quản lý hệ thống:

- Books (Sách)
- Users (Người dùng)
- Reviews (Đánh giá)

API được thiết kế và tài liệu hóa dựa trên chuẩn **OpenAPI 3.0**.

Các file chính trong project:

- `openapi.yaml` : OpenAPI specification
- `README.md` : Hướng dẫn sử dụng tài liệu API

---

## Yêu cầu hệ thống

Để chạy các công cụ liên quan đến OpenAPI bạn cần:

- Node.js >= 16
- npm hoặc npx
- Docker (khuyến nghị)
- Trình duyệt web

---

# Hướng dẫn sử dụng các công cụ (Tools)

OpenAPI có nhiều công cụ giúp:

- Xem tài liệu API
- Sinh client code
- Test API
- Mock API server

Dưới đây là các công cụ phổ biến.

---

# 1. Xem tài liệu trực quan (API Documentation)

Thay vì đọc trực tiếp file `openapi.yaml`, bạn có thể render thành giao diện web.

## Sử dụng Swagger UI

```bash
npx swagger-ui-watcher openapi.yaml
```

Sau đó mở trình duyệt:

```
http://localhost:3000
```

Swagger UI cho phép:

- Xem danh sách endpoint
- Xem request parameters
- Xem request body
- Xem response schema
- Test API trực tiếp

---

## Sử dụng Redoc

Redoc cung cấp giao diện documentation rõ ràng và dễ đọc.

### Chạy Redoc

```bash
npx redoc-cli serve openapi.yaml
```

Sau đó mở trình duyệt:

```
http://localhost:8080
```

Redoc thường được dùng để publish tài liệu API.

---

# 2. Sinh Client Code (SDK)

OpenAPI cho phép tự động generate client code cho nhiều ngôn ngữ.

Tool phổ biến: **OpenAPI Generator**

Repository:

```
https://github.com/OpenAPITools/openapi-generator
```

---

## Cài đặt OpenAPI Generator

### Cài bằng npm

```bash
npm install @openapitools/openapi-generator-cli -g
```

### Hoặc sử dụng Docker

```bash
docker pull openapitools/openapi-generator-cli
```

---

## Generate TypeScript Client

```bash
npx @openapitools/openapi-generator-cli generate \
-i openapi.yaml \
-g typescript-axios \
-o ./client
```

Sau khi generate sẽ có cấu trúc:

```
client/
 ├── apis/
 ├── models/
 ├── api.ts
 └── index.ts
```

---

## Generate Python Client

```bash
npx @openapitools/openapi-generator-cli generate -i openapi.yaml -g python -o ./python-client
```

Các ngôn ngữ hỗ trợ:

- Typescript
- Java
- Python
- Go
- Kotlin
- C#
- PHP

---

# 3. Test API bằng Postman

Postman có thể import trực tiếp file OpenAPI.

## Bước 1

Mở Postman.

## Bước 2

Chọn:

```
Import
```

## Bước 3

Upload file:

```
openapi.yaml
```

Postman sẽ tự tạo:

- Collection
- Request
- Example response

Sau đó bấm:

```
Send
```

để test API.

---

# 4. Test API bằng Insomnia

Insomnia cũng hỗ trợ OpenAPI.

## Bước 1

Chọn:

```
Create → Import
```

## Bước 2

Chọn:

```
From OpenAPI Specification
```

## Bước 3

Upload:

```
openapi.yaml
```

Insomnia sẽ tự động tạo toàn bộ endpoints.

---

# 5. Mock API Server

Khi backend chưa hoàn thành, bạn có thể tạo mock API server từ OpenAPI.

Tool phổ biến: **Prism**

Repository:

```
https://github.com/stoplightio/prism
```

---

## Cài đặt Prism

```bash
npm install -g @stoplight/prism-cli
```

---

## Chạy Mock Server

```bash
prism mock openapi.yaml
```

Server sẽ chạy tại:

```
http://localhost:4010
```

Ví dụ:

```
GET http://localhost:4010/books
```

Prism sẽ trả dữ liệu mock dựa trên schema trong OpenAPI.

---

# 6. Cấu trúc thư mục đề xuất

```
book-management-api/

 ├── openapi.yaml
 ├── api.apib
 ├── README.md

 ├── docs/
 │    └── api-docs

 ├── client/
 │    └── typescript-client

 ├── mock/
 │    └── prism

 └── backend/
```

---

# 7. Workflow phát triển API

Quy trình phát triển API thường dùng:

1. Thiết kế API bằng OpenAPI
2. Render documentation bằng Swagger hoặc Redoc
3. Generate client SDK
4. Mock API server
5. Backend implement API
6. Test API bằng Postman hoặc Insomnia

Cách làm này được gọi là **API-first development**.

---

# 8. Tổng kết

OpenAPI giúp:

- Chuẩn hóa thiết kế API
- Tạo documentation tự động
- Generate client SDK
- Mock API server
- Hỗ trợ frontend phát triển trước backend

Nhờ đó việc phát triển và tích hợp API trở nên nhanh và dễ quản lý hơn.
