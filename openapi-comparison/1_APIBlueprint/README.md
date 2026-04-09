# Book Management API - API Blueprint

## Giới thiệu

Thư mục này chứa tài liệu API được viết bằng **API Blueprint**.

API Blueprint là một định dạng mô tả REST API dạng Markdown giúp:

- Viết tài liệu API dễ đọc
- Render thành giao diện documentation
- Sinh mock server
- Test API

File chính:

- `api.apib` : API Blueprint specification

---

## Yêu cầu hệ thống

Để sử dụng các công cụ API Blueprint cần:

- Node.js >= 16
- npm hoặc npx
- Trình duyệt web

---

# Hướng dẫn sử dụng các công cụ (Tools)

API Blueprint có nhiều công cụ để:

- Render API documentation
- Tạo mock server
- Test API
- Validate API specification

Dưới đây là các công cụ phổ biến.

---

# 1. Xem tài liệu API (Documentation)

API Blueprint có thể render thành giao diện web.

## Sử dụng Aglio

Aglio là tool phổ biến để render API Blueprint.

### Cài đặt

```bash
npm install -g aglio
```

### Render documentation

```bash
aglio -i api.apib -o index.html
```

hoặc

```bash
npx aglio -i api.apib -o index.html
```

Sau khi chạy xong sẽ tạo file:

```
index.html
```

Mở file bằng trình duyệt để xem tài liệu API.

---

## Chạy server preview

Bạn cũng có thể chạy server preview trực tiếp.

```bash
aglio -i api.apib -s
```

Sau đó mở:

```
http://localhost:3000
```

---

# 2. Kiểm tra API Blueprint (Lint / Validate)

Bạn có thể kiểm tra file API Blueprint có hợp lệ hay không.

Tool: **Drafter**

### Cài đặt

```bash
npm install -g drafter
```

### Validate file

```bash
drafter api.apib
```

Nếu file hợp lệ, Drafter sẽ parse và hiển thị cấu trúc AST.

---

# 3. Tạo Mock API Server

Bạn có thể chạy mock server từ API Blueprint.

Tool phổ biến: **Drakov**

### Cài đặt

```bash
npm install -g drakov
```

---

## Chạy mock server

```bash
drakov -f api.apib
```

Server sẽ chạy tại:

```
http://localhost:3000
```

Ví dụ:

```
GET http://localhost:3000/books
```

Drakov sẽ trả response mock dựa trên định nghĩa trong `api.apib`.

---

# 4. Test API bằng Postman

Bạn có thể test API sau khi mock server chạy.

## Bước 1

Mở Postman.

## Bước 2

Tạo request mới.

## Bước 3

Gửi request tới mock server:

```
GET http://localhost:3000/books
```

Hoặc:

```
POST http://localhost:3000/books
```

Postman sẽ hiển thị response được định nghĩa trong API Blueprint.

---

# Test API bằng Dredd và chuyển đổi API Blueprint sang OpenAPI

Phần này hướng dẫn cách:

1. Convert API Blueprint sang OpenAPI
2. Test API bằng **Dredd**
3. Sử dụng **npx** thay vì cài đặt global bằng npm

---

## 1. Convert API Blueprint sang OpenAPI

Nếu API được viết bằng **API Blueprint (`api.apib`)**, bạn có thể chuyển sang **OpenAPI (`openapi.yaml`)** để sử dụng với nhiều công cụ hơn.

Tool phổ biến: **apib2swagger**

### Convert sang OpenAPI

```bash
npx --yes apib2swagger -i api.apib --yaml -o openapi.yaml
```

Sau khi chạy, bạn sẽ có file:

```
openapi.yaml
```

File này có thể dùng với:

- Swagger UI
- Redoc
- OpenAPI Generator
- Prism
- Schemathesis

---

## 2. Cài đặt và sử dụng Dredd

Dredd là công cụ kiểm thử API dựa trên **API specification**.

Dredd sẽ:

1. đọc OpenAPI hoặc API Blueprint
2. gửi request tới API server
3. so sánh response với specification

---

### Chạy Dredd với OpenAPI

```bash
npx dredd openapi.yaml http://localhost:5000
```

Dredd sẽ gửi request tới server tại:

```
http://localhost:5000
```

và kiểm tra response.

---

### Chạy Dredd với API Blueprint

Bạn cũng có thể test trực tiếp từ file Blueprint:

```bash
npx dredd api.apib http://localhost:5000
```

---

## 3. Ví dụ workflow hoàn chỉnh

Ví dụ workflow test API từ Blueprint:

```
1. Convert Blueprint sang OpenAPI
npx apib2swagger api.apib > openapi.yaml

2. Chạy API server
npm start

3. Test API bằng Dredd
npx dredd openapi.yaml http://localhost:5000
```

---

## 4. Ví dụ output của Dredd

Sau khi chạy test, terminal sẽ hiển thị kết quả:

```
GET /books
✓ 200 OK

POST /books
✓ 201 Created

GET /books/{id}
✓ 200 OK
```

Nếu API trả sai response:

```
GET /books
✗ Expected status code 200 but got 500
```

---

## 5. Lợi ích của việc dùng Dredd

Dredd giúp:

- Test API tự động
- Kiểm tra API đúng specification
- Phát hiện lỗi integration
- Dễ tích hợp vào CI/CD

Dredd hoạt động tốt với:

- OpenAPI
- API Blueprint
- CI pipelines
- automated API testing

# 5. Cấu trúc file API Blueprint

Một file API Blueprint thường có cấu trúc như sau:

```
FORMAT: 1A
HOST: http://localhost:3000

# Book Management API

## Books Collection [/books]

### List all books [GET]

+ Response 200 (application/json)

        [
            {
                "id": 1,
                "title": "Example Book"
            }
        ]
```

Các thành phần chính gồm:

- Resource
- Request
- Response
- Parameters
- Example data

---

# 6. Cấu trúc thư mục đề xuất

```
book-management-api/

 ├── openapi.yaml
 ├── api.apib
 ├── README.md

 ├── docs/
 │    └── api-docs

 ├── mock/
 │    └── drakov

 └── backend/
```

---

# 7. Workflow sử dụng API Blueprint

Quy trình phát triển API thường dùng:

1. Thiết kế API bằng `api.apib`
2. Render documentation bằng Aglio
3. Validate bằng Drafter
4. Chạy mock server bằng Drakov
5. Backend implement API
6. Test API bằng Postman

Workflow này giúp:

- Thiết kế API rõ ràng
- Frontend có thể làm việc trước backend
- Giảm lỗi tích hợp API

---

# 8. Tổng kết

API Blueprint là một công cụ đơn giản để mô tả API bằng Markdown.

Ưu điểm:

- Dễ viết
- Dễ đọc
- Có thể render thành documentation
- Hỗ trợ mock server
- Phù hợp cho API-first development
