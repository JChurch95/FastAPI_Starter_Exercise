from fastapi import FastAPI

app = FastAPI()

# Create our root route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Add a new GET endpoint
# It will accept a path parameter
@app.get("/items/{item_id}")
# Define the data type to return the proper data
# int will return an integer
def read_item(item_id: int):
    return {"item_id": item_id}

# Query Parameters? Sure!
@app.get("/items/")
# Define multiple data types
# We can also setup for query parameters
def read_items(skip: int = 0, limit: int = 10, q: str = None):
    if q:
        return {"skip": skip, "limit": limit, "q": q}
    else:
        return {"skip": skip, "limit": limit}

# Can this route take path parameters too? Yep!
@app.get("/users/{user_id}")
def read_user_items(user_id):
    return {"user_id": user_id}

# Path & Query Parameters? Why not!
@app.get("/users/{user_id}/items/")
def read_user_items(user_id, skip, limit):
    return {"user_id": user_id, "skip": skip, "limit": limit}

# Use this command to run the api locally
# uvicorn main:app --reload
