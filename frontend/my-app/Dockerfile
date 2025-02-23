# 1. ベースイメージの選択
FROM node:latest

# 2. 作業ディレクトリの設定
WORKDIR /app

# 4. ソースコードのコピー
COPY . .

# 3. 依存関係のコピーとインストール
COPY package*.json ./
RUN npm install

# 5. ポートの公開
EXPOSE 3000

# 6. アプリケーションの起動コマンド
CMD ["npm", "start"]