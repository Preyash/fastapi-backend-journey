from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Middleware for logging requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Request: {request.method} {request.url} - Completed in {process_time:.4f}s - Status: {response.status_code}")
    return response

# Exception handler for a custom exception
class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    logger.error(f"CustomException occurred: {exc.name}")
    return JSONResponse(
        status_code=400,
        content={
            "message": f"Oops! {exc.name} did something wrong.",
            "code": "CUSTOM_ERROR"
        },
    )

# Example endpoint that might raise a custom exception
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 13:
        raise CustomException(name="ThirteenError")
    return {"item_id": item_id}

# Example endpoint for basic health check
@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called.")
    return {"status": "healthy"}

# Example endpoint with a simulated delay
@app.get("/slow")
async def slow_endpoint():
    time.sleep(2) # Simulate a blocking I/O operation
    logger.info("Slow endpoint completed.")
    return {"message": "This was a slow response"}

# Example endpoint that causes an unhandled exception
@app.get("/error")
async def error_endpoint():
    logger.error("Error endpoint called, raising an unhandled exception.")
    raise ValueError("This is an unhandled error!")

# To run this application:
# uvicorn day14_observability:app --reload
# Test with:
# curl http://127.0.0.1:8000/health
# curl http://127.0.0.1:8000/items/12
# curl http://127.0.0.1:8000/items/13
# curl http://127.0.0.1:8000/slow
# curl http://127.0.0.1:8000/error
