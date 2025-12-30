import asyncio
import time

async def io_task():
    await asyncio.sleep(3)

async def main():
    start = time.time()
    await asyncio.gather(io_task(), io_task())
    print("Total time:", time.time() - start)

asyncio.run(main())


# def cpu_task():
#     count = 0
#     for i in range(10_000_000):
#         count += i
#     return count

# async def main():
#     start = time.time()
#     cpu_task()
#     cpu_task()
#     print("Total time:", time.time() - start)

# asyncio.run(main())


# Why didn’t async help CPU work?
# bcz it is asynchronous

# What happens if CPU work runs inside FastAPI?
# it will block the event loop

# How would this affect 1,000 users?
# it will take more time to handle more resources


# 🔥 Real-World FastAPI Rule (MEMORIZE THIS)
# Async = IO-bound
# Sync / Workers = CPU-bound
# In FastAPI:
# DB calls → async
# Heavy logic → background workers / separate services


# Why CPU work blocks the event loop
# bcz its synchronous hence sequence of tasks will block the flow

# When async should NOT be used
# in CPU-bound tasks like Heavy calculations, Image processing, Encryption, Large loops
