import { z } from "zod";

/* Models */
export const Book = z.object({
  id: z.number(),
  title: z.string(),
  author: z.string(),
});

export const User = z.object({
  id: z.number(),
  username: z.string(),
  email: z.string(),
});

export const Review = z.object({
  id: z.number(),
  rating: z.number(),
  comment: z.string(),
  book_id: z.number(),
  user_id: z.number(),
});

/* Inputs */
export const BookInput = Book.omit({ id: true });
export const UserInput = User.omit({ id: true });
export const ReviewInput = Review.omit({ id: true });

/* Example usage */
const newBook = BookInput.parse({
  title: "Test",
  author: "Someone",
});

console.log(newBook);
