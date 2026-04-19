from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

# 1. The Dependency (The Security Guard)
def verify_api_key(api_key: str):
    # Use == for value comparison
    if api_key != "london-python":
        # We raise the error here so the main function stays clean
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return True

# 2. The Route
@app.get("/secure-data")
async def get_data(authorized: bool = Depends(verify_api_key)):
    # If we reach this line, we KNOW the user is authorized.
    # No if/else needed here!
    return {"data": "This is top secret info"}