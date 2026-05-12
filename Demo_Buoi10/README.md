# Demo_Buoi10

Project nay dung Flask Python, sao chep nhom API chinh tu Demo_Buoi3 va co the trien khai bang Docker.

Da co san:

- API `books`, `users`, `book-reviews`
- Logging co ban bang Python `logging`
- Monitoring co ban bang Prometheus qua `prometheus_client`
- Dockerfile va `docker-compose.yml` de chay nhanh

## 1. Cai dat local

Yeu cau:

- Python 3.10+
- Docker neu muon chay bang container

Cai dependencies:

```bash
pip install -r requirements.txt
```

## 2. Chay local

Khoi dong app:

```bash
python run.py
```

Mac dinh server chay o:

- `http://localhost:5000`

## 3. Chay bang Docker

Build va run bang Docker Compose (API + Prometheus):

```bash
docker compose up --build
```

Sau khi len, ban co:

- API Flask: `http://localhost:5000`
- Prometheus UI: `http://localhost:9090`

Hoac neu muon build image rieng cho API:

```bash
docker build -t demo_buoi10 .
docker run -p 5000:5000 demo_buoi10
```

## 4. Chay demo_requests

Script `demo_requests.ps1` dung de goi lan luot nhieu API request de demo nhanh toan bo he thong.

Chay script nay khi app da dang chay local hoac trong Docker:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\demo_requests.ps1
```

Script se thuc hien cac buoc sau:

- Kiem tra `GET /health`
- Lay danh sach `books` va `users`
- Tao moi `book`, `user`, `review`
- Goi `GET /metrics` de xem metrics do Prometheus thu thap

Sau khi chay xong, ban co the mo `logs/app.log` de xem log request va mo `http://localhost:9090` de xem metrics.

## 5. Logging

App dung `logging` cua Python va cau hinh trong `app/logging_config.py`.

Noi dung logging hoat dong nhu sau:

- Moi request se duoc ghi nhan sau khi tra response
- Log se in ra console va dong thoi ghi vao file `logs/app.log`
- Dinh dang log co timestamp, muc do log, ten logger va message
- File log duoc xoay vong nho `RotatingFileHandler`, nen khong bi phat to vo han

Ban co the xem log theo hai cach:

- Mo terminal dang chay app va quan sat dong log moi khi goi API
- Mo file `logs/app.log` de xem lich su request

Demo logging nhanh:

1. Chay app bang `python run.py` hoac `docker compose up --build`
2. Goi mot API, vi du:

```bash
curl http://localhost:5000/api/v1/books
```

3. Kiem tra terminal hoac `logs/app.log`, ban se thay dong log co thong tin nhu:

```text
2026-05-12 18:10:52,554 INFO app HTTP request
```

Y nghia cua dong log:

- `method`: phuong thuc HTTP, vi du `GET`
- `route`: duong dan route da xu ly, vi du `/api/v1/books`
- `status_code`: ma trang thai tra ve, vi du `200`
- `duration_ms`: thoi gian xu ly request tinh theo mili giay

## 6. Monitoring voi Prometheus

Prometheus duoc cai dat trong `app/monitoring/metrics.py`.

Co hai metric chinh:

- `http_requests_total`: dem tong so request theo `method`, `route`, `status_code`
- `http_request_duration_seconds`: do thoi gian xu ly tung request tinh bang giay; day la histogram nen no khong chi cho mot gia tri duy nhat ma gom request vao cac khoang thoi gian khac nhau

Ngoai ra, endpoint `/metrics` con xuat them mot so default metrics cua Python process.

Demo Prometheus trong project nay don gian la: app se tu dong cap nhat metric moi khi co request, sau do `demo_requests.ps1` goi nhieu endpoint lien tiep va cuoi cung truy cap `/metrics` de ban thay ro so request da tang va latency duoc chia theo bucket.

### Cach chay Prometheus

Phan monitor duoc chay bang service `prometheus` trong `docker-compose.yml` va dung file cau hinh `prometheus/prometheus.yml`.

Service nay se scrape metrics tu service `api` qua:

- `http://api:5000/metrics`

### Endpoint metrics

- `GET /metrics`

### Demo monitoring nhanh

1. Chay app
2. Goi mot vai API:

```bash
curl http://localhost:5000/health
curl http://localhost:5000/api/v1/books
curl http://localhost:5000/api/v1/books/1
```

3. Mo:

```bash
curl http://localhost:5000/metrics
```

4. Tim cac dong metric sau:

- `http_requests_total`
- `http_request_duration_seconds`

Ban se thay thong ke theo tung route, vi du:

```text
http_requests_total{method="GET",route="/api/v1/books",status_code="200"} 1
```

Va histogram do latency:

```text
http_request_duration_seconds_bucket{le="0.005",method="GET",route="/api/v1/books",status_code="200"} 1
```

- `http_request_duration_seconds_bucket`: dem so request co thoi gian xu ly nho hon hoac bang mot nguong `le` cu the, vi du `0.005` giay, `0.01` giay, `0.05` giay... Nhieu bucket duoc cong lai de biet request nhanh hay cham va phan bo latency ra sao.

Neu ban muon dua vao Prometheus server that, chi can cau hinh scrape job tro toi `http://<host>:5000/metrics`.

### Su dung Prometheus UI

Mo `http://localhost:9090` va thu cac truy van sau trong tab Graph:

```promql
http_requests_total
```

```promql
http_request_duration_seconds_bucket
```

Hoac loc theo route:

```promql
http_requests_total{route="/api/v1/books"}
```

Neu ban goi API nhieu lan, gia tri `http_requests_total` se tang dan va histogram latency se hien theo bucket.

## 7. API chinh

### Books

- `GET /api/v1/books`
- `GET /api/v1/books/:book_id`
- `POST /api/v1/books`
- `DELETE /api/v1/books/:book_id`

Body tao book:

```json
{
  "title": "Domain-Driven Design",
  "author": "Eric Evans"
}
```

### Users

- `GET /api/v1/users`
- `GET /api/v1/users/:user_id`
- `POST /api/v1/users`
- `DELETE /api/v1/users/:user_id`

Body tao user:

```json
{
  "username": "charlie",
  "email": "charlie@example.com"
}
```

### Reviews

- `GET /api/v1/book-reviews`
- `GET /api/v1/book-reviews/:review_id`
- `POST /api/v1/book-reviews`

Body tao review:

```json
{
  "rating": 5,
  "comment": "Excellent",
  "book_id": 1,
  "user_id": 1
}
```

## 8. Health check

- `GET /health`

Tra ve:

```json
{ "status": "ok" }
```
