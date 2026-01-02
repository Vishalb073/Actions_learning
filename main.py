import asyncio
import logging
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_google import GoogleAugmentedLLM

# Enable debug logging to see tool calls in the GitHub console
logging.basicConfig(level=logging.DEBUG)

async def main():
    server_config = {
        "playwright": {
            "command": "npx",
            "args": ["-y", "@playwright/mcp@latest"]
        }
    }

    with open("mission.txt", "r") as f:
        mission = f.read()

    # Create the agent
    agent = Agent(
        name="QA_Agent",
        instruction=(
            "You are a real browser automation agent. "
            "You MUST use your tools for EVERY step. "
            "If you cannot find a tool, stop and report an error. "
            f"Mission: {mission}"
        ),
        servers=server_config
    )

    llm = GoogleAugmentedLLM(agent=agent)
    
    # DEBUG: List tools to ensure Playwright is actually connected
    # This will print to your GitHub Actions log
    print("--- Available Tools ---")
    # Some versions use agent.list_tools(), others require checking the server context
    # We will let the LLM verify this by asking it
    
    print("🚀 Running Mission with Tool-Tracing...")
    # Using a structured prompt to force tool usage
    response = await llm.generate_str(
        "List the tools you have access to, then execute the mission. "
        "For every tool you call, describe the result you received from the browser."
    )
    
    print(f"\n--- FINAL REPORT ---\n{response}")

if __name__ == "__main__":
    asyncio.run(main())
