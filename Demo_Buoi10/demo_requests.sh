#!/bin/bash

# Script demo - goi nhieu API request va xem logging/metrics

BASE_URL="http://localhost:5000"

echo "========================================"
echo "Demo Buoi10 - Multiple API Requests"
echo "========================================"
echo ""

# 1. Health check
echo "[1] GET /health"
curl -s "$BASE_URL/health" | jq '.' || curl -s "$BASE_URL/health"
echo ""
echo ""

# 2. Get all books
echo "[2] GET /api/v1/books"
curl -s "$BASE_URL/api/v1/books" | jq '.' || curl -s "$BASE_URL/api/v1/books"
echo ""
echo ""

# 3. Create a new book
echo "[3] POST /api/v1/books - tao book moi"
curl -s -X POST "$BASE_URL/api/v1/books" \
  -H "Content-Type: application/json" \
  -d '{"title":"Microservices Patterns","author":"Chris Richardson"}' | jq '.' || \
curl -s -X POST "$BASE_URL/api/v1/books" \
  -H "Content-Type: application/json" \
  -d '{"title":"Microservices Patterns","author":"Chris Richardson"}'
echo ""
echo ""

# 4. Get all users
echo "[4] GET /api/v1/users"
curl -s "$BASE_URL/api/v1/users" | jq '.' || curl -s "$BASE_URL/api/v1/users"
echo ""
echo ""

# 5. Create a new user
echo "[5] POST /api/v1/users - tao user moi"
curl -s -X POST "$BASE_URL/api/v1/users" \
  -H "Content-Type: application/json" \
  -d '{"username":"david","email":"david@example.com"}' | jq '.' || \
curl -s -X POST "$BASE_URL/api/v1/users" \
  -H "Content-Type: application/json" \
  -d '{"username":"david","email":"david@example.com"}'
echo ""
echo ""

# 6. Get a specific book
echo "[6] GET /api/v1/books/1 - lay chi tiet book"
curl -s "$BASE_URL/api/v1/books/1" | jq '.' || curl -s "$BASE_URL/api/v1/books/1"
echo ""
echo ""

# 7. Create a review
echo "[7] POST /api/v1/book-reviews - tao review moi"
curl -s -X POST "$BASE_URL/api/v1/book-reviews" \
  -H "Content-Type: application/json" \
  -d '{"rating":5,"comment":"Amazing book on microservices","book_id":1,"user_id":1}' | jq '.' || \
curl -s -X POST "$BASE_URL/api/v1/book-reviews" \
  -H "Content-Type: application/json" \
  -d '{"rating":5,"comment":"Amazing book on microservices","book_id":1,"user_id":1}'
echo ""
echo ""

# 8. Get all reviews
echo "[8] GET /api/v1/book-reviews - lay tat ca review"
curl -s "$BASE_URL/api/v1/book-reviews" | jq '.' || curl -s "$BASE_URL/api/v1/book-reviews"
echo ""
echo ""

# 9. Get metrics
echo "[9] GET /metrics - xem prometheus metrics (hien chi tiet)"
echo "Relevant metrics:"
curl -s "$BASE_URL/metrics" | grep -E "http_requests_total|http_request_duration_seconds_bucket" | head -20
echo ""
echo ""

echo "========================================"
echo "Demo completed!"
echo "Check logs/app.log for logging details"
echo "Open Prometheus: http://localhost:9090"
echo "Query: http_requests_total"
echo "========================================"
