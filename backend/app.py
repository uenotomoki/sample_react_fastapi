from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Reactアプリなどからのアクセスを許可するオリジンを設定します
origins = [
    "http://localhost",
    "http://localhost:3000",  # Reactのデフォルトポート
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "https://sample-react-ij37.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 送信されるデータのスキーマを定義（例として、messageというフィールドを受け取る）
class Data(BaseModel):
    message: str

# GETリクエスト（リクエストボディなし）
@app.get("/")
async def root():
    # GETでは通常リクエストボディは使わないため、固定のレスポンスを返す
    return {"status": "success", "data": "data_root_url"}

# POSTリクエストでデータを受け取るエンドポイント
@app.post("/api/endpoint")
async def post_data(data: Data):
    # 受け取ったデータをコンソールに表示
    print("Received data:", data.message)
    # 受信内容をレスポンスとして返す
    return {"status": "success", "data": data.message}