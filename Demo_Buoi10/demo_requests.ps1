# Script demo - goi nhieu API request va xem logging/metrics

$BASE_URL = "http://localhost:5000"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Demo Buoi10 - Multiple API Requests" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. Health check
Write-Host "[1] GET /health" -ForegroundColor Green
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/health"
Write-Host "Response: $($response.Content)" -ForegroundColor Yellow
Write-Host ""

# 2. Get all books
Write-Host "[2] GET /api/v1/books" -ForegroundColor Green
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/api/v1/books"
Write-Host "Response: $($response.Content)" -ForegroundColor Yellow
Write-Host ""

# 3. Create a new book
Write-Host "[3] POST /api/v1/books - tao book moi" -ForegroundColor Green
$bookBody = @{
    title = "Microservices Patterns"
    author = "Chris Richardson"
} | ConvertTo-Json
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/api/v1/books" `
    -Method POST -ContentType "application/json" -Body $bookBody
Write-Host "Response: $($response.Content)" -ForegroundColor Yellow
Write-Host ""

# 4. Get all users
Write-Host "[4] GET /api/v1/users" -ForegroundColor Green
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/api/v1/users"
Write-Host "Response: $($response.Content)" -ForegroundColor Yellow
Write-Host ""

# 5. Create a new user
Write-Host "[5] POST /api/v1/users - tao user moi" -ForegroundColor Green
$userBody = @{
    username = "david"
    email = "david@example.com"
} | ConvertTo-Json
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/api/v1/users" `
    -Method POST -ContentType "application/json" -Body $userBody
Write-Host "Response: $($response.Content)" -ForegroundColor Yellow
Write-Host ""

# 6. Get a specific book
Write-Host "[6] GET /api/v1/books/1 - lay chi tiet book" -ForegroundColor Green
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/api/v1/books/1"
Write-Host "Response: $($response.Content)" -ForegroundColor Yellow
Write-Host ""

# 7. Create a review
Write-Host "[7] POST /api/v1/book-reviews - tao review moi" -ForegroundColor Green
$reviewBody = @{
    rating = 5
    comment = "Amazing book on microservices"
    book_id = 1
    user_id = 1
} | ConvertTo-Json
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/api/v1/book-reviews" `
    -Method POST -ContentType "application/json" -Body $reviewBody
Write-Host "Response: $($response.Content)" -ForegroundColor Yellow
Write-Host ""

# 8. Get all reviews
Write-Host "[8] GET /api/v1/book-reviews - lay tat ca review" -ForegroundColor Green
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/api/v1/book-reviews"
Write-Host "Response: $($response.Content)" -ForegroundColor Yellow
Write-Host ""

# 9. Delete a book
Write-Host "[9] DELETE /api/v1/books/1 - xoa book" -ForegroundColor Green
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/api/v1/books/1" `
    -Method DELETE
Write-Host "Status: $($response.StatusCode)" -ForegroundColor Yellow
Write-Host ""

# 10. Get metrics
Write-Host "[10] GET /metrics - xem prometheus metrics" -ForegroundColor Green
$response = Invoke-WebRequest -UseBasicParsing -Uri "$BASE_URL/metrics"
$metrics = $response.Content
# Extract relevant metrics
$relevantMetrics = $metrics | Select-String -Pattern "http_requests_total|http_request_duration_seconds_bucket" -AllMatches
Write-Host "Extracted metrics:" -ForegroundColor Yellow
$relevantMetrics.Matches | ForEach-Object { Write-Host $_.Value -ForegroundColor Yellow }
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Demo completed! Check logs/app.log" -ForegroundColor Cyan
Write-Host "Open Prometheus: http://localhost:9090" -ForegroundColor Cyan
Write-Host "Query: http_requests_total" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
