from fastapi import FastAPI, Depends
app = FastAPI()

def get_resource():
    print("🔌 Resource created")
    resource = {"connection": "open"}
    try:
        yield resource
    finally:
        print("❌ Resource closed")

@app.get("/use-resource")
async def use_resource(res=Depends(get_resource)):
    return {"status": "using resource", "resource": res}

# What problem does Depends solve?
# Depends solves the problem of dependency injection. It allows you to define dependencies that can be injected into your endpoints, making your code more modular and testable.

# Why shouldn’t we use global connections?
# It lead to issues such as resource leaks, connection timeouts, and make your code harder to test and maintain.

# Why does cleanup run even if request fails?
# Because FastAPI uses context managers to manage resources.

# Why is this perfect for DB connections?
# Use when needed & release when not needed.

# What breaks if cleanup doesn’t happen?
# resource leaks & connection timeouts.

# what are request-scoped resources?
# created once per request and destroyed when the request is finished.

# why this is safer than globals?
# because it's limited to the scope of the request.

# 🔥 Real-World Mapping
# DB session → yield
# Auth token decode → Depends
# Permissions → chained dependencies
# Cleanup → automatic
