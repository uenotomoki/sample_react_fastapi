# backend/Dockerfile

FROM python:3.9-slim
WORKDIR /app

# 必要なライブラリをインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
# アプリケーションファイルをコピー
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]