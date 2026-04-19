from pydantic import BaseModel, Field, EmailStr
#basemodel gives it a strict contract and we use field and emailstr to write validation using pyndatics
class UserSchema(BaseModel):
    #eg. using field we wrote a validation for the username in the model/class
    username: str = Field(..., min_length=3, max_length=20)
    email: str
    age: int | None = None


# What Pydantic does for you:
# Parsing: It converts the incoming JSON string into a Python object.
# Validation: It checks min_length, types, and required fields.
# Error Handling: If validation fails, it sends a 422 Unprocessable Entity response back to the client automatically. You don't write any "if" statements.


#real world backend example
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 1. The Schema (The Guard)
class Product(BaseModel):
    name: str = Field(..., example="Wireless Mouse")
    price: float = Field(..., gt=0) # Price must be 'Greater Than' 0
    category: str | None = "General" # Default value

# 2. The Database (Simulated for now)
db = []

@app.post("/products", status_code=201)
async def create_product(payload: Product):
    # 'payload' is an instance of the Product class
    product_dict = payload.dict() 
    db.append(product_dict)
    return {"message": "Created", "product": product_dict}

@app.get("/products")
async def list_products(limit: int = 5):
    # Slicing the list (Topic 1) based on the query parameter
    return db[:limit]

#how it works
payload = Product(name="keyboard", price=25 , category="General")
product_dict = payload.dict()

# then product_dict becomes
{
  "name": "Keyboard",
  "price": 25,
  "category": "General"
}
# later the append becomes
db.append(payload.dict())
[
  {
    "name": "Keyboard",
    "price": 25,
    "category": "General"
  }
]


# remember
# product_dict = payload.model_dump() 
# also works as a modern way .model_dump is same as .dict()