**Month 1: The FastAPI & Pydantic Foundations.**

---

### 1. The Architecture: Uvicorn vs. Node.js

In your **PERN** stack, you run `node index.js`. Node is the runtime and the server. 

In Python, we separate the **Code** from the **Server**. 
*   **FastAPI** is the code (the logic, the routes).
*   **Uvicorn** is the **ASGI Server** (Asynchronous Server Gateway Interface). 

**Why the separation?** 
Because Uvicorn is built to handle the "Waiter" logic (Topic 10: Async) at a very low level. It manages the "Event Loop" so your FastAPI code can focus entirely on data. In production in London, you will often see **Gunicorn** managing multiple **Uvicorn** workers. This is how Python scales to millions of users.

### 2. Pydantic: Not just a Class, but a "Validator"

In Express, if a user sends a JSON body, you usually have to write: 
`if (!req.body.name) return res.status(400)...`

In FastAPI, we use **Pydantic**. Pydantic is a data validation library. When you define a class inheriting from `BaseModel`, you are creating a **Strict Contract**.

```python
from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: str
    age: int | None = None
```

**What Pydantic does for you:**
1.  **Parsing:** It converts the incoming JSON string into a Python object.
2.  **Validation:** It checks `min_length`, types, and required fields.
3.  **Error Handling:** If validation fails, it sends a **422 Unprocessable Entity** response back to the client automatically. You don't write any "if" statements.

### 3. The Path vs. Query Parameters

In backend development, you need to get data from the URL. FastAPI makes this "Type Safe."

*   **Path Parameters:** For specific resources. 
    `@app.get("/users/{user_id}")` -> `async def get_user(user_id: int):`
    *FastAPI will crash the request if `user_id` is not an integer.*
*   **Query Parameters:** For filtering or searching.
    `@app.get("/search")` -> `async def search(q: str, limit: int = 10):`
    *This maps to `/search?q=python&limit=10`.*

---

### Real-World Backend Example: The Product API

Imagine you are building the backend for an e-commerce site. You need to handle incoming product data and ensure it is safe before saving it.

```python
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
```

---

### Your Coding Challenge: The "AI Prompt Manager"

Since you want to be an **AI Engineer**, let's build a more complex API that handles AI "Prompts."

**Task:**
1.  **Setup:** Create a `FastAPI` instance.
2.  **Schema:** Create a Pydantic model `AIRequest`.
    *   `prompt`: String (Must be at least 10 characters long).
    *   `model_name`: String (Default to `"gpt-3.5-turbo"`).
    *   `token_limit`: Integer (Must be between 1 and 4000).
3.  **POST Route:** Create a route `/process-prompt`.
    *   It should accept the `AIRequest`.
    *   It should return a dictionary containing the original prompt and a fake "ai_response" string.
4.  **GET Route:** Create a route `/models/{category}`.
    *   It should take a path parameter `category`.
    *   It should take a query parameter `provider` (string).
    *   Return: `{"message": f"Fetching {category} models from {provider}"}`.

** answers can be found in 2aipromptmanager_challange.py**
**Senior Constraints:**
*   Use **Type Hints** for all function arguments and return types.
*   Make all route functions **async**.
*   Use `Field` from `pydantic` to enforce the `min_length` and `token_limit` rules.

---

### 🧠 Deep Checkpoint Questions:

1.  **FastAPI vs Express:** In Express, `req.body` is just a plain object. In FastAPI, what is the advantage of the `payload` being a Pydantic object? (Think about autocomplete and attributes).
2.  **The Docs:** Once you write this code and run it, what URL do you visit to see the **Automatic Swagger Documentation**? (This is a huge part of the London dev workflow).
3.  **Validation:** If a user sends a `token_limit` of `5000` to your API, who stops the request? Is it your function logic or Pydantic?

**Answer**
**Corrected on the code but this review points are useful for learning**

Since you are a **PERN** developer, I am going to review this like a **Senior Engineer reviewing a Pull Request (PR)**. I will show you where the code would crash and how to fix it to meet London production standards.

---

### 🚩 Senior Code Review

#### 1. Pydantic `Field` Keywords
*   **Your Code:** `Field(..., min=1, max=4000)`
*   **The Issue:** Pydantic doesn't use `min` and `max` for numbers. It uses **`ge`** (Greater than or Equal) and **`le`** (Less than or Equal).
*   **The Fix:** `Field(..., ge=1, le=4000)`

#### 2. Decorator Metadata
*   **Your Code:** `@app.post("/process-prompt", AIRequest)`
*   **The Issue:** The second part of the decorator is for "Metadata" (like the status code). You don't put the Model name there. FastAPI knows which model to use by looking at your function arguments.
*   **The Fix:** `@app.post("/process-prompt")`

#### 3. Path Parameter Syntax
*   **Your Code:** `async def list_category(/category, provider: str):`
*   **The Issue:** This is a syntax error. In Python, function arguments are just names. You don't use a `/`. The name must match exactly what you put in the `{curly_braces}` in the URL.
*   **The Fix:** `async def list_category(category: str, provider: str):`

#### 4. The `.dict()` vs `.model_dump()`
*   **The Tip:** In Pydantic V1, we used `.dict()`. In the modern **Pydantic V2** (which you should use), we use **`.model_dump()`**. It does the same thing but is the new standard.

---

### The Corrected "Production" Version

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class AIRequest(BaseModel):
    # '...' means this field is REQUIRED
    prompt: str = Field(..., min_length=10)
    model_name: str = "gpt-3.5-turbo"
    # ge = greater than or equal | le = less than or equal
    token_limit: int = Field(..., ge=1, le=4000)

@app.post("/process-prompt")
async def create_prompt(request_data: AIRequest):
    # Convert Pydantic object to a standard Python Dictionary
    data_dict = request_data.model_dump() 
    
    return {
        "message": "ai_response", 
        "prompt_received": data_dict["prompt"],
        "config": data_dict
    }

@app.get("/model/{category}")
async def list_category(category: str, provider: str):
    # category comes from the URL path: /model/chat
    # provider comes from the Query String: ?provider=openai
    return {"message": f"Fetching {category} models from {provider}"}
```

---

### 🎓 Answers to your 3 Questions

You asked to understand these deeply. These are common **interview questions** for Junior/Mid Python roles in London.

#### Q1: In Express, `req.body` is a plain object. In FastAPI, what is the advantage of `request_data` being a Pydantic object?

**The Senior Answer:**
In Express, `req.body` is just "blind data." Your code editor (VS Code) doesn't know what is inside it, so you get no autocomplete.
In FastAPI, because `request_data` is an **Instance of a Class** (Topic 4), your editor knows exactly which fields exist. If you type `request_data.` it will suggest `prompt` and `token_limit`. 
Also, Pydantic objects are **Type-Safe**. You can add methods to them to calculate data or clean strings before they ever reach your logic.

#### Q2: What URL do you visit to see the Automatic Swagger Documentation?

**The Senior Answer:**
You visit **`/docs`**. 
FastAPI automatically reads your Pydantic models and your routes and builds an interactive website. You can actually test your `POST` requests directly from this page without using Postman or building a React frontend first. There is also a second version at **`/redoc`**.

#### Q3: If a user sends a `token_limit` of `5000`, who stops the request?

**The Senior Answer:**
**Pydantic stops it.** 
The request never even enters your `create_prompt` function. FastAPI acts as a "Bouncer" at the door. It sees the data is wrong, creates a clear error message, and sends a `422 Unprocessable Entity` response back to the user. This keeps your "Business Logic" clean because you don't have to write validation code inside your functions.

---
