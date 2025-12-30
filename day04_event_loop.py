import asyncio

async def task(name):
    print(f"{name}: start")
    await asyncio.sleep(2)
    print(f"{name}: end")

# def blocking_task():
#     import time
#     time.sleep(3)

# async def bad_task():
#     blocking_task()
#     print("This blocks everything")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C"),
        # bad_task()
    )

asyncio.run(main())

# Why does async help IO-bound work?
# Because of asynchronous process, it will handle more resources. 

# Why is CPU work dangerous inside async APIs?
# async doesn't work with cpu-bound tasks, so flow will be blocked.

# Why is time.sleep() dangerous in FastAPI?
# It uses synchronous handling, so it will block the execution flow.

# Why is await asyncio.sleep() safe?
# It utilizes asynchronous task handling so it won't block the whole flow. It will pause and switch to another task.

# What happens if 1 request blocks the loop?
# It will stall the whole process.

# 🔥 GOLDEN FASTAPI RULE
# If it waits -> async
# If it thinks -> dont run in event loop
