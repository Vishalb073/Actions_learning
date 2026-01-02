import asyncio
import os
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_google import GoogleAugmentedLLM

async def main():
    # 1. Setup the Playwright Server configuration
    # This tells the agent how to launch the 'browser hands'
    server_config = {
        "playwright": {
            "command": "npx",
            "args": ["-y", "@playwright/mcp@latest"]
        }
    }

    # 2. Initialize the Agent directly
    # We pass the mission.txt content as the main instruction
    with open("mission.txt", "r") as f:
        mission = f.read()

    agent = Agent(
        name="QA_Agent",
        instruction=f"You are a QA specialist. Follow these steps: {mission}",
        servers=server_config
    )

    # 3. Attach the Gemini Brain and Execute
    # The library will automatically look for GOOGLE_API_KEY in the environment
    print("🚀 Connecting to Gemini and starting browser...")
    
    # Using the direct initialization pattern
    llm = GoogleAugmentedLLM(agent=agent)
    
    print("📝 Executing Mission...")
    result = await llm.generate_str("Please start the playwright browser and follow the mission instructions.")
    
    print(f"\n--- MISSION RESULT ---\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
