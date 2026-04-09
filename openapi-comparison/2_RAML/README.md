# Tạo API Documentation cho RAML

Phần này hướng dẫn cách tạo **API Documentation từ file RAML (`api.raml`)** bằng công cụ CLI chạy trên terminal.  
Các bước bao gồm:

1. Viết RAML specification
2. Generate documentation
3. Xem API documentation trên trình duyệt

Tất cả các lệnh đều sử dụng **npx** để tránh phải cài global package.

---

# 1. Ví dụ RAML Specification

File RAML thường có dạng:

```
api.raml
```

Ví dụ:

```yaml
#%RAML 1.0
title: Book Management API
version: v1
baseUri: http://localhost:3000

/books:
  get:
    description: Get list of books
    responses:
      200:
        body:
          application/json:
            example: |
              [
                {
                  "id": 1,
                  "title": "Example Book"
                }
              ]

  post:
    description: Create a new book
    body:
      application/json:
        example: |
          {
            "title": "New Book"
          }
    responses:
      201:
        body:
          application/json:
            example: |
              {
                "id": 2,
                "title": "New Book"
              }
```

---

# 2. Tạo API Documentation bằng raml2html

Tool phổ biến để tạo documentation từ RAML là **raml2html**.

## Generate documentation

```bash
npx --yes raml2html -i api.raml -o index.html
```

Sau khi chạy lệnh, hệ thống sẽ tạo file:

```
index.html
```

---

# 3. Xem API Documentation

Mở file bằng trình duyệt:

```
index.html
```

Trang documentation sẽ hiển thị:

- API title
- endpoint list
- request method
- request body
- response example

---

# 4. Chạy local server để xem docs

Nếu muốn chạy documentation qua server:

```bash
npx serve .
```

Sau đó mở:

```
http://localhost:3000
```

---

# 5. Convert RAML sang OpenAPI (tùy chọn)

Nếu muốn sử dụng thêm các tool khác như Swagger UI hoặc Dredd, bạn có thể convert RAML sang OpenAPI.

```bash
npx --yes oas-raml-converter --from RAML --to OAS20 api.raml | npx --yes json2yaml > openapi.yaml
```

Sau đó có thể dùng:

```
Swagger UI
Redoc
Prism
Dredd
OpenAPI Generator
```

# 6. Workflow sử dụng RAML

Ví dụ workflow khi phát triển API:

```
1. Thiết kế API
api.raml

2. Generate documentation
npx --yes raml2html -i api.raml -o index.html

3. Chạy server để xem docs
npx serve .

4. Convert sang OpenAPI nếu cần
npx --yes oas-raml-converter --from RAML --to OAS20 api.raml | npx --yes json2yaml > openapi.yaml
```

---

# 7. Cấu trúc thư mục đề xuất

```
book-management-api/

 ├── api.raml
 ├── index.html
 ├── openapi.yaml
 ├── README.md

 └── docs/
```

---

# Tổng kết

RAML hỗ trợ:

- thiết kế API bằng YAML
- generate documentation
- convert sang OpenAPI
- tích hợp với các công cụ test API

Các tool thường dùng với RAML:

| Tool         | Chức năng                  |
| ------------ | -------------------------- |
| raml2html    | Generate API documentation |
| raml2openapi | Convert RAML sang OpenAPI  |
| Dredd        | Test API specification     |
| Prism        | Mock API server            |
