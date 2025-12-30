from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Day 6 - Path & Query Params"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "type": str(type(user_id))}

@app.get("/search")
async def search_users(active: bool = True, page: int = 1):
    return {"active": active, "page": page}

# Why is user_id automatically an int?
# bcz type hinting

# Why does FastAPI reject /users/abc?
# bcz user_id has int type

# Why are query params optional?
# bcz they have default values

# path params = resource identity
# query params = filter & navigation
