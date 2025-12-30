from fastapi import FastAPI, BackgroundTasks
import time
app = FastAPI()

def write_log(message: str):
    try:
        time.sleep(5)
        print(f"📄 Log written: {message}")
    except Exception as e:
        print(f"❌ Task failed: {e}")

@app.get("/process")
async def process_data(bg_tasks: BackgroundTasks):
    bg_tasks.add_task(write_log, "Data processed")
    return {"message": "Task started"}

# Why didn’t the client wait?
# ans: bcz it is a background task

# What happens if background task fails?
# task is lost forever.

# Why shouldn’t we use this for heavy jobs?
# they too risky. If the server restarts, that task is lost forever.

# Dependencies = business logic
# Middleware = infrastructure logic
