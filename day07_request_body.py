from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
async def create_user(user: UserCreate):
    return {
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

# Why didn’t we manually parse JSON?
# bcz pydantic

# Where did validation happen?
# bcz pydantic

# Why is this safer than dict-based input
# pydantic
