import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace

load_dotenv()

agent = Agent(
    name="jokester",
    instructions="you are a joke teller",
    model="gpt-4o-mini"
)

async def joke_teller():
    result = await Runner.run(
        starting_agent=agent,
        input="tell me a joke"
    )
    print("\n🎭 Joke Result:")
    print(result.final_output)
    return result

async def main():
    with trace("joke_agent_trace"):
        result = await joke_teller()
        print("\n✅ Agent execution completed")

if __name__ == "__main__":
    asyncio.run(main())
