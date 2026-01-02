import asyncio
from mcp_agent.agents.agent import Agent
from mcp_agent.app import MCPApp


async def main():
    # Initialize the app with your config
    app = MCPApp(name="RegressionSuite")

    # Create the agent with your "Mission"
    async with app.run_server_context("npx -y @playwright/mcp") as context:
        agent = Agent(
            name="QA-Agent",
            instructions=open("mission.txt").read(),
            model="gemini-1.5-flash"
        )
        # Execute the mission
        result = await agent.run()
        print(result)


if __name__ == "__main__":
    asyncio.run(main())