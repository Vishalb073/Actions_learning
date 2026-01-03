import asyncio
import os
import sys
from browser_use import Agent
# FIX: Import ChatGoogle from browser_use instead of langchain directly
from browser_use.llm import ChatGoogle 

async def main():
    # Initialize the LLM using the browser-use wrapper
    # It will automatically look for the GOOGLE_API_KEY env var
  langchain_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Pass it to browser-use
# Note: Ensure you are using the latest version of browser-use
llm = langchain_llm

    # Define the mission
    mission = (
        "Go to https://s2-www.orangehealth.dev/. "
        "1. Extract and log all unique links from the homepage. "
        "2. Search for 'CBC' in the search bar and check the price. "
        "3. If any step fails, report 'FAILURE'. "
        "Take a screenshot of the results page."
    )

    agent = Agent(
        task=mission,
        llm=llm,
    )

    # Run the mission
    history = await agent.run()
    
    # Check for success/failure to control GitHub Action status
    final_result = history.final_result()
    if final_result and "FAILURE" in final_result.upper():
        print("❌ Mission failed.")
        sys.exit(1)
    
    print("✅ Mission successful.")

if __name__ == "__main__":
    asyncio.run(main())
