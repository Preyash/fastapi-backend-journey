from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()

fake_users = {
    1: {'name': 'preyash', 'email': 'test@email.com'}
}

class UserResponse(BaseModel):
    name: str
    email: str

@app.get('/users/{user_id}', response_model=UserResponse)
async def get_user(user_id: int):
    user = fake_users.get(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user

@app.post('/user', status_code=status.HTTP_201_CREATED)
async def create_user():
    return {'message': 'user created'}


# What’s the difference between request & response models?
# request models validate incoming data, response models validate outgoing data

# Why do we hide fields in responses?
# bcz we don't want to expose sensitive data

# Why not return 200 for errors?
# bcz its for Successful req

# How does frontend benefit from proper status codes?
# users can get a precise idea of what went wrong

# Why is 422 automatic but 404 manual?
# bcz 422 is for validation errors, 404 is for not found errors

# | Code | Meaning          | When to use      |
# | ---- | ---------------- | ---------------- |
# | 200  | OK               | Successful GET   |
# | 201  | Created          | Successful POST  |
# | 400  | Bad Request      | Invalid input    |
# | 401  | Unauthorized     | Not logged in    |
# | 403  | Forbidden        | No permission    |
# | 404  | Not Found        | Resource missing |
# | 422  | Validation Error | FastAPI auto     |
# | 500  | Server Error     | Bug / crash      |
