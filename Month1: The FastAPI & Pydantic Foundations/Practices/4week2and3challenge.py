from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

# 1. THE SCHEMA (The Inspector)
class Product(BaseModel):
    name: str
    price: float
    stock_count: int

# 2. DEPENDENCY 1: The Bouncer (Security)
# We tell FastAPI to look in the Headers for 'x-admin-token'
def verify_admin(x_admin_token: str = Header(...)):
    if x_admin_token != "secret-key":
        # Raise an error to stop the request immediately
        raise HTTPException(status_code=403, detail="Invalid Admin Token")
    return "Admin_Verified"

# 3. DEPENDENCY 2: The Toolbox (Database)
def get_db():
    print("LOG: [START] Opening Fake Database Connection...")
    db_connection = "POSTGRES_DB_V1"
    try:
        yield db_connection  # Hand the connection to the route
    finally:
        print("LOG:[END] Closing Database Connection...")

# 4. THE ROUTE (The Worksite)
@app.post("/admin/add-product")
async def create_product(
    product: Product,                          # Inspector checks the JSON body
    admin_status: str = Depends(verify_admin), # Bouncer checks the Header
    db: str = Depends(get_db)                  # Toolbox provides the Database
):
    # If the code reaches this line, we KNOW the JSON is valid, 
    # the user is an admin, and the DB is open!
    
    return {
        "message": f"Successfully added {product.name}",
        "price": product.price,
        "security_status": admin_status,
        "saved_to": db
    }