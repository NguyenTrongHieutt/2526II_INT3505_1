import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi3";

using TypeSpec.Http;
using TypeSpec.Rest;

@service(#{
  title: "Book Management API"
})
@server("http://127.0.0.1:5000", "Production server")
@doc("API for managing books, users, and reviews")
namespace BookManagementAPI;

// ==========================================
// MODELS (Khai báo cấu trúc & Dữ liệu mẫu)
// ==========================================

model Meta {
  @example("2026-01-01T12:00:00")
  timestamp: string;
}

model Book {
  @example(1)
  id?: int32;
  @example("Clean Code")
  title: string;
  @example("Robert C. Martin")
  author: string;
}

model BookInput {
  @example("Clean Code")
  title: string;
  @example("Robert C. Martin")
  author: string;
}

model User {
  @example(1)
  id?: int32;
  @example("nguyenvan_a")
  username: string;
  @example("nguyenvana@email.com")
  email: string;
}

model UserInput {
  @example("nguyenvan_a")
  username: string;
  @example("nguyenvana@email.com")
  email: string;
}

model Review {
  @example(1)
  id?: int32;
  @example(5)
  rating: int32;
  @example("Một cuốn sách tuyệt vời, rất đáng đọc!")
  comment: string;
  @example(1)
  book_id: int32;
  @example(1)
  user_id: int32;
}

model ReviewInput {
  @example(5)
  rating: int32;
  @example("Một cuốn sách tuyệt vời, rất đáng đọc!")
  comment: string;
  @example(1)
  book_id: int32;
  @example(1)
  user_id: int32;
}

// ==========================================
// GENERICS (Tái sử dụng cấu trúc Response)
// ==========================================

model SingleResponse<T> {
  data: T;
  meta: Meta;
}

model ListResponse<T> {
  data: T[];
  meta: Meta;
}

// ==========================================
// ENDPOINTS (Khai báo API & Giá trị mẫu cho ID)
// ==========================================

@route("/api/v1/books")
interface Books {
  @get
  @summary("Get list of books")
  list(): { @statusCode _: 200, @body body: ListResponse<Book> };

  @post
  @summary("Create new book")
  create(@body body: BookInput): { @statusCode _: 201, @body response: SingleResponse<Book> };

  @route("/{book_id}")
  @get
  @summary("Get book by ID")
  getById(@path @example(1) book_id: int32): { @statusCode _: 200, @body body: SingleResponse<Book> } | { @statusCode _: 404 };

  @route("/{book_id}")
  @delete
  @summary("Delete book")
  delete(@path @example(1) book_id: int32): { @statusCode _: 204 } | { @statusCode _: 404 };
}

@route("/api/v1/users")
interface Users {
  @get
  @summary("Get list of users")
  list(): { @statusCode _: 200, @body body: ListResponse<User> };

  @post
  @summary("Create new user")
  create(@body body: UserInput): { @statusCode _: 201, @body response: SingleResponse<User> };

  @route("/{user_id}")
  @get
  @summary("Get user by ID")
  getById(@path @example(1) user_id: int32): { @statusCode _: 200, @body body: SingleResponse<User> } | { @statusCode _: 404 };

  @route("/{user_id}")
  @delete
  @summary("Delete user")
  delete(@path @example(1) user_id: int32): { @statusCode _: 204 } | { @statusCode _: 404 };
}

@route("/api/v1/book-reviews")
interface Reviews {
  @get
  @summary("Get list of reviews")
  list(): { @statusCode _: 200, @body body: ListResponse<Review> };

  @post
  @summary("Create review")
  create(@body body: ReviewInput): { @statusCode _: 201, @body response: SingleResponse<Review> };

  @route("/{review_id}")
  @get
  @summary("Get review by ID")
  getById(@path @example(1) review_id: int32): { @statusCode _: 200, @body body: SingleResponse<Review> } | { @statusCode _: 404 };

  @route("/{review_id}")
  @delete
  @summary("Delete review")
  delete(@path @example(1) review_id: int32): { @statusCode _: 204 } | { @statusCode _: 404 };
}