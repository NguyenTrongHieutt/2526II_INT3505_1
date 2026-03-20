# SLIDE CONTENT

## 1. Tổng quan

Có nhiều cách để mô tả API:

- Spec-based (OpenAPI, RAML)
- Documentation-based (API Blueprint)
- Code-first (TypeSpec, TypeAPI)

---

## 2. So sánh cú pháp

| Format    | Kiểu       | Đặc điểm       |
| --------- | ---------- | -------------- |
| OpenAPI   | YAML       | Chuẩn, verbose |
| Blueprint | Markdown   | Dễ đọc         |
| RAML      | YAML       | Structured     |
| TypeSpec  | Code       | Typed          |
| TypeAPI   | TypeScript | Runtime        |

👉 Nhận xét:

- Blueprint dễ đọc nhất
- OpenAPI chi tiết nhất
- TypeSpec gần code nhất

---

## 3. Độ dễ học

| Format    | Đánh giá   |
| --------- | ---------- |
| OpenAPI   | ⭐⭐⭐     |
| Blueprint | ⭐⭐⭐⭐⭐ |
| RAML      | ⭐⭐⭐     |
| TypeSpec  | ⭐⭐⭐     |
| TypeAPI   | ⭐⭐⭐⭐   |

👉 Nhận xét:

- Blueprint dễ học nhất
- TypeSpec cần biết syntax riêng

---

## 4. Khả năng biểu diễn

| Format    | Schema     | Validation |
| --------- | ---------- | ---------- |
| OpenAPI   | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Blueprint | ⭐         | ⭐         |
| RAML      | ⭐⭐⭐⭐   | ⭐⭐⭐⭐   |
| TypeSpec  | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| TypeAPI   | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

👉 Nhận xét:

- OpenAPI + TypeSpec mạnh nhất
- Blueprint yếu nhất

---

## 5. Tooling

| Format    | Tool             |
| --------- | ---------------- |
| OpenAPI   | Swagger, Postman |
| Blueprint | Aglio            |
| RAML      | RAML Viewer      |
| TypeSpec  | Compiler         |
| TypeAPI   | Zod              |

👉 Nhận xét:

- OpenAPI có ecosystem mạnh nhất

---

## 6. Ứng dụng thực tế

| Format    | Production |
| --------- | ---------- |
| OpenAPI   | ⭐⭐⭐⭐⭐ |
| Blueprint | ⭐⭐       |
| RAML      | ⭐⭐       |
| TypeSpec  | ⭐⭐⭐⭐   |
| TypeAPI   | ⭐⭐⭐⭐   |

👉 Nhận xét:

- OpenAPI là tiêu chuẩn industry
- TypeSpec đang nổi lên

---

## 7. Ưu / Nhược điểm

### OpenAPI

- Chuẩn phổ biến
- Tool mạnh

* Dài, khó đọc

### API Blueprint

- Dễ đọc

* Thiếu tính năng

### RAML

- Structured tốt

* Ít phổ biến

### TypeSpec

- Code-first
- Generate mạnh

* Còn mới

### TypeAPI

- Dùng trực tiếp backend

* Không phải spec chuẩn

---

## 8. Kết luận

👉 Nếu chọn 1:

- Production → OpenAPI
- Dev experience → TypeSpec
- Backend validation → TypeAPI
- Documentation nhanh → Blueprint

👉 Xu hướng:

- Chuyển từ spec → code-first (TypeSpec)
