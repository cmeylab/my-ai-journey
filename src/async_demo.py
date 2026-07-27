import asyncio
async def say_hello(name:str)->str:
    await asyncio.sleep(1)
    return f"你好 {name}"
async def main()->None:
    print("开始...")
    results=await asyncio.gather(
        say_hello("Alice"),
        say_hello("Bob"),
        say_hello("Carol")
    )
    for r in results:
        print(r)
if __name__ == "__main__":
    asyncio.run(main())