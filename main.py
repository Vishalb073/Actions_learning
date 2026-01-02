import asyncio
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_google import GoogleAugmentedLLM

async def main():
    # 1. Read the mission from your text file
    with open("mission.txt", "r") as f:
        user_mission = f.read()

    # 2. Setup the Agent
    agent = Agent(
        name="QA_Agent",
        instruction=(
            "You are a QA Engineer. Use your browser tools to execute the steps "
            "provided in the mission. DO NOT just describe them; execute them. "
            "Always take a screenshot at the end of the mission."
        ),
        servers={
            "playwright": {
                "command": "npx",
                "args": ["-y", "@playwright/mcp@latest"]
            }
        }
    )

    llm = GoogleAugmentedLLM(agent=agent)
    
    # 3. Pass the file content to the AI
    print(f"🚀 Starting mission from mission.txt...")
    result = await llm.generate_str(user_mission)
    
    print(f"\n--- FINAL REPORT ---\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
