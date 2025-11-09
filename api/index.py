from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Sample REST API",
    description="FastAPI sample application deployed on Vercel",
    version="1.0.0"
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# データモデル
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    created_at: Optional[str] = None

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    created_at: Optional[str] = None

# インメモリデータストア
items_db: List[Item] = [
    Item(id=1, name="サンプル商品1", description="これは商品1です", price=1000, created_at=datetime.now().isoformat()),
    Item(id=2, name="サンプル商品2", description="これは商品2です", price=2000, created_at=datetime.now().isoformat()),
]

users_db: List[User] = [
    User(id=1, username="user1", email="user1@example.com", created_at=datetime.now().isoformat()),
    User(id=2, username="user2", email="user2@example.com", created_at=datetime.now().isoformat()),
]

# ルートエンドポイント
@app.get("/")
async def root():
    """
    ルートエンドポイント - APIの情報を返す
    """
    return {
        "message": "FastAPI REST API Sample",
        "version": "1.0.0",
        "endpoints": {
            "items": "/api/items",
            "users": "/api/users",
            "health": "/api/health"
        }
    }

# ヘルスチェック
@app.get("/api/health")
async def health_check():
    """
    ヘルスチェックエンドポイント
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

# Items エンドポイント
@app.get("/api/items", response_model=List[Item])
async def get_items():
    """
    全ての商品を取得
    """
    return items_db

@app.get("/api/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """
    特定の商品を取得
    """
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/api/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    """
    新しい商品を作成
    """
    # 新しいIDを生成
    new_id = max([i.id for i in items_db], default=0) + 1
    item.id = new_id
    item.created_at = datetime.now().isoformat()
    items_db.append(item)
    return item

@app.put("/api/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    """
    既存の商品を更新
    """
    for index, item in enumerate(items_db):
        if item.id == item_id:
            updated_item.id = item_id
            updated_item.created_at = item.created_at
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/api/items/{item_id}")
async def delete_item(item_id: int):
    """
    商品を削除
    """
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# Users エンドポイント
@app.get("/api/users", response_model=List[User])
async def get_users():
    """
    全てのユーザーを取得
    """
    return users_db

@app.get("/api/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """
    特定のユーザーを取得
    """
    user = next((user for user in users_db if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/api/users", response_model=User, status_code=201)
async def create_user(user: User):
    """
    新しいユーザーを作成
    """
    # 新しいIDを生成
    new_id = max([u.id for u in users_db], default=0) + 1
    user.id = new_id
    user.created_at = datetime.now().isoformat()
    users_db.append(user)
    return user

@app.put("/api/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    """
    既存のユーザーを更新
    """
    for index, user in enumerate(users_db):
        if user.id == user_id:
            updated_user.id = user_id
            updated_user.created_at = user.created_at
            users_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/users/{user_id}")
async def delete_user(user_id: int):
    """
    ユーザーを削除
    """
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(index)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
