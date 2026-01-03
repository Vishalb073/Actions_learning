import asyncio
import sys
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
import os

async def main():
    # 1. Setup the Gemini Vision Model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=SecretStr(os.getenv("GOOGLE_API_KEY"))
    )

    # 2. Define the Agent and the Mission
    mission = (
        "Go to https://s2-www.orangehealth.dev/. "
        "1. Find and log all unique links on the homepage. "
        "2. Search for 'CBC' in the search box. "
        "3. Find the price for 'CBC'. "
        "4. If you cannot find the search box or the price, explicitly say 'MISSION_FAILED'. "
        "Take a screenshot of the results."
    )

    agent = Agent(
        task=mission,
        llm=llm,
    )

    # 3. Run the mission
    history = await agent.run()
    
    # 4. Check for Failure
    final_result = history.final_result()
    print(f"Final Report: {final_result}")

    if "MISSION_FAILED" in final_result or not history.is_done():
        print("❌ Regression Test Failed!")
        sys.exit(1)
    
    print("✅ Regression Test Passed!")

if __name__ == "__main__":
    asyncio.run(main())
