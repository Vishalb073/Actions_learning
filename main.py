import asyncio
from browser_use import Agent

async def main():
    agent = Agent(
        model="gpt-4.1-mini",
        task="Open https://s2-www.orangehealth.dev/  "
             "search for body check ups and add full body checkup in cart and validate pricing also add new random phone number , "
             "add otp 3291 and customer details if it is asking and give me dom snapshots so that i can validate dom"


    )

    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
