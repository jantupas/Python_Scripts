import asyncio


async def main():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")
    return_value = await task
    print(f"Return value was: {return_value}")


async def other_function():
    print("1")
    # wait for this statement to finish
    await asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())
