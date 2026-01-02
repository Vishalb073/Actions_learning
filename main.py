import asyncio
import os
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_google import GoogleAugmentedLLM

async def main():
    # 1. Initialize the App
    app = MCPApp(name="QA_Automation")

    # 2. Define the Agent and tell it which server to use
    # We define the server directly here for simplicity
    playwright_server = {
        "playwright": {
            "command": "npx",
            "args": ["-y", "@playwright/mcp@latest"]
        }
    }

    async with app:
        # Create the agent
        agent = Agent(
            name="Playwright_Tester",
            instruction=open("mission.txt").read(),
            server_names=["playwright"]
        )

        async with agent:
            # Connect Gemini to the Agent
            llm = await agent.attach_llm(GoogleAugmentedLLM)
            
            # Execute the mission
            print("--- Starting Mission ---")
            result = await llm.generate_str("Please execute the mission.txt instructions now.")
            print(f"--- Mission Result ---\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
