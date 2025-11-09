# FastAPI REST API Sample for Vercel

FastAPIを使用したREST APIのサンプルプロジェクトです。Vercelにデプロイすることができます。

## 機能

- ✅ FastAPIによるREST API
- ✅ CRUD操作のサンプル（Items、Users）
- ✅ Pydanticによるデータバリデーション
- ✅ CORS対応
- ✅ 自動生成されるAPI ドキュメント（Swagger UI）
- ✅ Vercelへのデプロイ対応

## プロジェクト構造

```
vercel-restapi-test/
├── api/
│   └── index.py        # FastAPIアプリケーション
├── requirements.txt    # Pythonパッケージの依存関係
├── vercel.json        # Vercelデプロイ設定
└── README.md          # このファイル
```

## APIエンドポイント

### 基本エンドポイント

- `GET /` - API情報
- `GET /api/health` - ヘルスチェック

### Items（商品）エンドポイント

- `GET /api/items` - 全商品の取得
- `GET /api/items/{item_id}` - 特定商品の取得
- `POST /api/items` - 商品の作成
- `PUT /api/items/{item_id}` - 商品の更新
- `DELETE /api/items/{item_id}` - 商品の削除

### Users（ユーザー）エンドポイント

- `GET /api/users` - 全ユーザーの取得
- `GET /api/users/{user_id}` - 特定ユーザーの取得
- `POST /api/users` - ユーザーの作成
- `PUT /api/users/{user_id}` - ユーザーの更新
- `DELETE /api/users/{user_id}` - ユーザーの削除

## ローカル開発

### 前提条件

- Python 3.9以上

### セットアップ

1. リポジトリのクローン

```bash
git clone <repository-url>
cd vercel-restapi-test
```

2. 仮想環境の作成と有効化

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

4. 開発サーバーの起動

```bash
uvicorn api.index:app --reload
```

5. ブラウザで以下のURLにアクセス

- API: http://localhost:8000
- Swagger UI（APIドキュメント）: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Vercelへのデプロイ

### 方法1: Vercel CLI

1. Vercel CLIのインストール

```bash
npm i -g vercel
```

2. デプロイ

```bash
vercel
```

### 方法2: GitHub連携（推奨）

1. このリポジトリをGitHubにプッシュ
2. [Vercel](https://vercel.com)にアクセスしてログイン
3. "New Project"をクリック
4. GitHubリポジトリをインポート
5. デプロイ設定は自動的に検出されます
6. "Deploy"をクリック

デプロイ後、以下のようなURLでアクセスできます：
- `https://your-project.vercel.app/`
- `https://your-project.vercel.app/docs` （APIドキュメント）

## APIの使用例

### 商品の取得

```bash
curl https://your-project.vercel.app/api/items
```

### 商品の作成

```bash
curl -X POST https://your-project.vercel.app/api/items \
  -H "Content-Type: application/json" \
  -d '{
    "name": "新商品",
    "description": "新しい商品の説明",
    "price": 3000
  }'
```

### 商品の更新

```bash
curl -X PUT https://your-project.vercel.app/api/items/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "更新された商品",
    "description": "更新された説明",
    "price": 3500
  }'
```

### 商品の削除

```bash
curl -X DELETE https://your-project.vercel.app/api/items/1
```

## 技術スタック

- **FastAPI** - モダンで高速なPython Webフレームワーク
- **Pydantic** - データバリデーションと型ヒント
- **Uvicorn** - ASGI サーバー
- **Vercel** - デプロイメントプラットフォーム

## 注意事項

- このサンプルではデータをインメモリで保持しています。本番環境では適切なデータベースを使用してください。
- Vercelの無料プランでは、サーバーレス関数の実行時間に制限があります（10秒）。
- 環境変数を使用する場合は、Vercelのダッシュボードから設定してください。

## ライセンス

MIT
