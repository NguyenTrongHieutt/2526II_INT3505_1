# Demo_Buoi7 - OpenAPI Generator (FastAPI) + MongoDB

Muc tieu folder nay:

- Docker chi chay MongoDB
- Sinh backend FastAPI tu OpenAPI bang OpenAPI Generator
- Khong dung script rieng, chi chay lenh truc tiep

## 1) File can dung

- openapi.yaml
- docker-compose.yml
- .env
- .env.example
- README.md

## 2) Dieu kien can

- Docker Desktop
- Python 3.11+ (de chay backend sau khi generate)

Kiem tra nhanh:

```bash
py --version
docker --version
```

Khuyen nghi dung Python 3.12 cho project nay:

```bash
py -3.12 --version
```

## 3) Chay MongoDB bang Docker

Trong thu muc Demo_Buoi7:

```bash
docker compose up -d mongo
```

Kiem tra container:

```bash
docker ps
```

MongoDB se o:

```text
mongodb://127.0.0.1:27017
```

Dung MongoDB:

```bash
docker compose down
```

## 4) Bien moi truong

Noi dung .env mac dinh:

```env
APP_HOST=127.0.0.1
APP_PORT=8000
MONGO_URI=mongodb://127.0.0.1:27017/book_management
```

## 5) Sinh backend FastAPI bang OpenAPI Generator (khong dung Docker)

1. Tao virtual environment cho project (neu chua co):

```bash
py -3.12 -m venv .venv
```

2. Kich hoat env:

```bash
.venv\Scripts\activate
```

Neu da tao .venv bang Python 3.14 thi xoa va tao lai:

```powershell
Remove-Item -Recurse -Force .venv
py -3.12 -m venv .venv
.venv\Scripts\activate
```

3. Cai OpenAPI Generator CLI local:

```bash
pip install openapi-generator-cli
```

4. Sinh backend FastAPI:

```bash
openapi-generator-cli generate -i openapi.yaml -g python-fastapi -o backend_fastapi_generated
```

## 6) Chay backend FastAPI vua sinh

```bash
cd backend_fastapi_generated
pip install -r requirements.txt
uvicorn openapi_server.main:app --app-dir src --reload --host 127.0.0.1 --port 8000
```

Luu y Windows: uvloop khong ho tro Windows. Neu gap loi lien quan uvloop, mo file requirements trong thu muc generated va doi dong uvloop thanh:

```text
uvloop==0.21.0; platform_system != "Windows"
```

Neu gap loi build package C-extension nhu ujson/httptools (yeu cau Microsoft C++ Build Tools), hay dam bao ban dang dung .venv tao bang Python 3.12 thay vi 3.14.

Neu ban muon go `python` thay cho `py`, hay tat App execution aliases cho `python.exe` va `python3.exe` trong Windows Settings.

Neu template sinh ra entrypoint khac, mo README trong thu muc generated de dung dung lenh chay.

## 7) Viec can lam tiep sau khi generate

1. Tao module ket noi MongoDB dung MONGO_URI trong .env.
2. Thay code placeholder trong cac endpoint bang truy van MongoDB that.
3. Them validation request/response theo openapi.yaml.
4. Them xu ly loi va logging.
5. Viet test API.
6. Moi lan sua openapi.yaml thi generate lai va merge logic nghiep vu vao code.

## 8) Checklist demo nhanh

1. docker compose up -d mongo
2. tao va kich hoat .venv
   2.1 tao .venv bang py -3.12 -m venv .venv
3. pip install openapi-generator-cli
4. openapi-generator-cli generate -i openapi.yaml -g python-fastapi -o backend_fastapi_generated
5. cd backend_fastapi_generated
6. pip install -r requirements.txt
7. uvicorn openapi_server.main:app --app-dir src --reload --host 127.0.0.1 --port 8000
