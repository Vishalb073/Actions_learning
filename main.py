import asyncio
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_google import GoogleAugmentedLLM

async def main():
    # 1. Define the Playwright Server
    server_config = {
        "playwright": {
            "command": "npx",
            "args": ["-y", "@playwright/mcp@latest"]
        }
    }

    # 2. Define the Agent with strict instructions to use tools
    with open("mission.txt", "r") as f:
        mission = f.read()

    agent = Agent(
        name="QA_Agent",
        instruction=(
            "You are a QA automation executor. IMPORTANT: Do not write code. "
            "Use your provided browser tools (browser_navigate, browser_click, etc.) "
            "to perform the following mission on the live web. "
            f"Mission steps: {mission}"
        ),
        servers=server_config
    )

    # 3. Connect and Execute
    print("🚀 Connecting to Gemini Brain...")
    llm = GoogleAugmentedLLM(agent=agent)
    
    # We use a prompt that forces tool usage
    print("📝 Starting Browser-based Mission...")
    result = await llm.generate_str(
        "Start by navigating to the URL in the mission and use your tools to verify the elements. "
        "Report only the final PASS/FAIL status and any errors found."
    )
    
    print(f"\n--- FINAL REPORT ---\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
