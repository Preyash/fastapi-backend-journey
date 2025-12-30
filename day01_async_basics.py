import asyncio
import time

# Commented original async functions
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 'sample data'}

async def print_numbers():
    for i in range(3):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = fetch_data()
    task2 = print_numbers()
    results = await asyncio.gather(task1, task2)
    print('results', results)

# def non_async_fetch_data():
#     print('non-async start fetching')
#     time.sleep(2)
#     print('non-async done fetching')
#     return {'data': 'non-async sample data'}

# def non_async_print_numbers():
#     for i in range(3):
#         print(f'non-async {i}')
#         time.sleep(0.25)

# def non_async_main():
#     result = non_async_fetch_data()
#     non_async_print_numbers()
#     print('non-async result', result)

# non_async_main()


# Why didn’t the program block?
# because the program is not blocking, it is running in the background

# What happens if await is removed?
# the program will block, because the program is waiting for the fetch_data function to finish

# Why FastAPI prefers async?
# because it is faster, and it is more efficient
