from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Generator

app = FastAPI()

class Product(BaseModel):
    name: str
    price: int
    stock_count: int

def verify_admin(token: int):
    if token == "X-Admin-Token":
        try:
            yield db 
        finally:
            print("LOG: [3] Closing Database Session automatically.")

@app.post("/admin/add-product")
async def create_user(
    user_in: UserCreate, 
    db_conn: str = Depends(get_db_session) # <--- INJECTION HAPPENS HERE
):
    # This is the "Business Logic"
    print(f"LOG: [2] Using {db_conn} to save {user_in.username}")
    return {"status": "success", "user": user_in.username}
