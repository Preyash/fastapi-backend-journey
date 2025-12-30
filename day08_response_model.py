from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    name: str
    email: EmailStr

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    return {"name": user.name, "email": user.email, "password": user.password}


# What does a request model do?
# validate incoming data

# Where does validation happen?
# bcz of type hinting

# Why should passwords never be returned?
# it will reveal sensitive info, and account can be compromised

# What happens if DB returns extra fields?
# extra fields are ignored

# Why is response validation important for clients?
# bcz it ensures that the client is getting the data it expects
