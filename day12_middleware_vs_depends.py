from fastapi import FastAPI, Request, Depends
app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"➡️ Incoming request: {request.url.path}")
    response = await call_next(request)
    print(f"⬅️ Response sent")
    return response

@app.get("/ping")
async def ping():
    return {"message": "pong"}

def get_user():
    return {"username": "Preyash"}

@app.get("/profile")
async def profile(user=Depends(get_user)):
    return user

# What happens when a dependency uses yield?
# it is called, and the code inside it is executed.

# Why shouldn’t auth logging be middleware?
# it runs for every req

# Why shouldn’t DB sessions be middleware?
# it runs for every req

# What breaks if you mix responsibilities?
# the single responsibility principle

# | Problem     | Use        |
# | ----------- | ---------- |
# | Auth user   | Dependency |
# | DB session  | Dependency |
# | Logging     | Middleware |
# | Timing      | Middleware |
# | Permissions | Dependency |
# | Request ID  | Middleware |

# Golden rule:
# Dependencies = business logic
# Middleware = infrastructure logic
