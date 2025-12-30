from fastapi import FastAPI, Depends
app = FastAPI()

def get_current_user():
    return {"username": "Preyash"}

@app.get("/profile")
async def profile(user=Depends(get_current_user)):
    return {"message": "Profile data", "user": user}

@app.get("/settings")
async def settings(user=Depends(get_current_user)):
    return {"message": "Settings data", "user": user}


# Why are status codes part of API design?
# They distinguish between multiple levels of results

# Where does validation happen automatically?
# pydantic

# Why is Dependency Injection (DI) better than calling functions directly?
# It allows us to make code reusable and modular

# How would auth break without DI?
# It would be hard to test

# Why does DI improve testability?
# It makes it easier to test with testable endpoints
