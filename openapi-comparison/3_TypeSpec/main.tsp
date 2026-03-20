import "@typespec/http";

using Http;

model Book {
  id: int32;
  title: string;
  author: string;
}

model User {
  id: int32;
  username: string;
  email: string;
}

model Review {
  id: int32;
  rating: int32;
  comment: string;
  book_id: int32;
  user_id: int32;
}

@route("/api/v1/books")
namespace Books {
  @get op getBooks(): Book[];

  @post op createBook(@body body: Book): Book;

  @get op getBook(@path book_id: int32): Book;

  @delete op deleteBook(@path book_id: int32): void;
}

@route("/api/v1/users")
namespace Users {
  @get op getUsers(): User[];
  @post op createUser(@body body: User): User;
}

@route("/api/v1/book-reviews")
namespace Reviews {
  @get op getReviews(): Review[];
  @post op createReview(@body body: Review): Review;
}