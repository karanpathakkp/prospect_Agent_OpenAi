from agents import Agent, Runner
import asyncio
from dotenv import load_dotenv
import os
from tools import tavily_search, scrape_website

# Load environment variables from .env file
load_dotenv()

# Debug logging for API key
api_key = os.getenv("TAVILY_API_KEY")
if api_key:
    print("Tavily API key found in environment variables")
else:
    print("Tavily API key not found in environment variables")

async def main():
    # Read instructions from prompt.txt
    with open('prompt.txt', 'r') as file:
        instructions = file.read()

    karans_agent = Agent(
        name="Karans_Agent",
        instructions=instructions,
        model="gpt-4",
        tools=[tavily_search, scrape_website],
    )

    try:
        result4 = await Runner.run(karans_agent, "VP of R&D, Head of R&D, or the CIO—individuals who are key decision-makers in driving digital transformation and R&D initiatives.   company : Saudi Aramco", max_turns=2000)
        print(result4.final_output)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())



