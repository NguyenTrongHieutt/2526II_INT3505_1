# Tạo API Documentation với TypeSpec

Phần này hướng dẫn cách:

1. Thiết kế API bằng **TypeSpec**
2. Generate **OpenAPI specification**
3. Tạo **API documentation**
4. Sử dụng **npx** để chạy tool mà không cần cài global

TypeSpec là ngôn ngữ do **Microsoft** phát triển để mô tả API và có thể generate nhiều định dạng như:

- OpenAPI
- JSON Schema
- SDK
- API documentation

---

# 1. Khởi tạo Project TypeSpec

Sử dụng `npx` để quản lý phiên bản compiler mà không cần cài đặt global.

```bash
# Tạo thư mục dự án
mkdir api-design-lab && cd api-design-lab

# Khởi tạo package.json để npx hoạt động ổn định
npm init -y

# Cài đặt compiler TypeSpec (bản local)
npm install @typespec/compiler

# Khởi tạo cấu trúc dự án TypeSpec
# Khi hiện menu, chọn: "Generic REST API"
npx tsp init
```

---

Sau khi chạy lệnh, project sẽ có cấu trúc:

```

typespec-project/

├── main.tsp
├── package.json
├── tspconfig.yaml
└── node_modules/

```

---

# 2. Ví dụ TypeSpec API

File chính thường là:

```

main.tsp

```

Ví dụ API đơn giản:

```typespec
import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi3";

using TypeSpec.Http;

@service({
  title: "Book Management API"
})
namespace BookAPI;

model Book {
  id: int32;
  title: string;
}

@route("/books")
interface Books {

  @get
  list(): Book[];

  @post
  create(@body book: Book): Book;

}
```

---

# 3. Generate OpenAPI từ TypeSpec

TypeSpec có thể generate OpenAPI specification.

```bash
npx tsp compile .
```

Sau khi compile, file OpenAPI sẽ được tạo tại:

```
tsp-output/
```

---

# 4. Tạo API Documentation từ OpenAPI

Sau khi có file OpenAPI, bạn có thể tạo documentation bằng nhiều tool.

Ví dụ dùng **Redoc**:

```bash
npx redoc-cli serve tsp-output/@typespec/openapi3/openapi.yaml
```

Mở trình duyệt:

```
http://localhost:8080
```

---

# 5. Kiểm thử API bằng Schemathesis

Đây là công cụ tự động sinh dữ liệu "tra tấn" (Property-based Testing) để tìm lỗi logic và lỗi sập server (500).

## 5.1 Cài đặt bộ chạy `uv` (Siêu nhẹ & Sạch máy)

Sử dụng **`uv`** để chạy Schemathesis trong môi trường tạm thời mà không cần cài đặt Python thủ công. Mở **PowerShell** và chạy:

```powershell
powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
```

## 5.2 Chạy Test tự động (Zero Configuration)

Schemathesis sẽ tự động "đọc hiểu" file định nghĩa của bạn và bắt đầu test server.

```Bash
# Đảm bảo server Backend đang chạy (ví dụ tại port 5000)
# (uvx có thể thay bằng đường dẫn tới uvx.exe)
# "tsp-output/@typespec/openapi3/openapi.yaml" có thể thay bằng đường dẫn tới file OpenAPI của bạn
uvx schemathesis run "tsp-output/schema/openapi.yaml" --url http://localhost:5000
```

---

# 6. Workflow hoàn chỉnh

Ví dụ workflow sử dụng TypeSpec:

```
1. Thiết kế API
main.tsp

2. Compile TypeSpec
npx tsp compile .

3. Generate OpenAPI
tsp-output/@typespec/openapi3/openapi.yaml

4. Xem API documentation
npx redoc-cli serve tsp-output/@typespec/openapi3/openapi.yaml

5. Test API
npx dredd tsp-output/@typespec/openapi3/openapi.yaml http://localhost:3000
```

---

# 7. Cấu trúc thư mục đề xuất

```
book-management-api/

 ├── main.tsp
 ├── tspconfig.yaml
 ├── package.json

 ├── tsp-output/
 │    └── @typespec/
 │         └── openapi3/
 │              └── openapi.yaml

 ├── README.md
```

---

# Tổng kết

TypeSpec giúp:

- thiết kế API bằng ngôn ngữ mô tả mạnh mẽ
- generate OpenAPI specification
- tạo API documentation
- tích hợp testing và SDK generation

Các tool thường dùng với TypeSpec:

| Tool              | Chức năng         |
| ----------------- | ----------------- |
| TypeSpec Compiler | Compile TypeSpec  |
| OpenAPI Generator | Generate SDK      |
| Redoc             | API documentation |
| Dredd             | API testing       |
