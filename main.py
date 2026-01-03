import asyncio
import os
import sys
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

async def main():
    # 1. Setup the Gemini Model
    # We use ChatGoogleGenerativeAI directly but wrap it to avoid the 'provider' error
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=SecretStr(os.getenv("GOOGLE_API_KEY"))
    )

    # 2. Define the Mission (Ensuring consistent 4-space indentation)
    mission = (
        "Go to https://s2-www.orangehealth.dev/. "
        "1. Extract and log all unique links from the homepage. "
        "2. Search for 'CBC' in the search bar and check the price. "
        "3. If any step fails, report 'FAILURE'. "
        "Take a screenshot of the results page."
    )

    # 3. Initialize the Agent
    agent = Agent(
        task=mission,
        llm=llm,
    )

    # 4. Run the mission
    history = await agent.run()
    
    # 5. Handle GitHub Action Status
    final_result = history.final_result()
    print(f"Final Report: {final_result}")

    if final_result and "FAILURE" in final_result.upper():
        print("❌ Regression Test Failed!")
        sys.exit(1)
    
    print("✅ Regression Test Passed!")

if __name__ == "__main__":
    asyncio.run(main())
