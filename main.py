import asyncio
from browser_use import Agent

async def main():
    agent = Agent(
        model="gpt-4.1-mini",
        task = """
                1. Navigate to https://s2-www.orangehealth.dev/
                2. ASSERTION: Check if the search input with placeholder 'Search for tests' is visible. 
                   If not found, stop immediately and report 'FAILURE: Search box missing'.
                3. Search for 'CBC'.
                4. ASSERTION: Verify that at least one search result contains the text 'CBC'. 
                   If no results appear, report 'FAILURE: No search results for CBC'.
                5. Extract the price. 
                   If the price is greater than 1000, report 'FAILURE: Price too high'.
                """

    )

    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
