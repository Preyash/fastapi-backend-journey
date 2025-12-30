import time
import asyncio

# def task(name):
#     print(f"Start {name}")
#     time.sleep(2)
#     print(f"End {name}")
# start = time.time()
# task("A")
# task("B")
# print(f"Total time: {time.time() - start}s")

async def task(name):
    print(f"Start {name}")
    await asyncio.sleep(3)
    print(f"End {name}")
async def main():
    start = time.time()
    await asyncio.gather(
        task("A"),
        task("B")
    )
    print("Total time:", time.time() - start)
asyncio.run(main())

# What does async do?
# ans: async makes a function asynchronous

# What does await mean?
# ans: await means wait for the function to finish

# Why is FastAPI async-friendly?
# ans: FastAPI is async-friendly because it uses asyncio to handle requests

# asyncio is built-in in Python 3.7+
# asyncio is a library for writing concurrent code using the async/await syntax

# Why did async finish faster?
# bcz it is asynchronous

# What exactly happened during await?
# execution flow paused and switched to another task

# Why would sync code be dangerous in an API?
# it will take more time to handle more resources

# async programming (with asyncio) is incredibly beneficial for:
# I/O-bound operations : Tasks that spend most of their time waiting for external resources, such as:
#    - Network requests (e.g., fetching data from APIs, web scraping)
#    - Database queries
#    - File I/O
#    - Long-running external processes

# Async doesn’t make code faster — it makes waiting smarter.
