from dotenv import load_dotenv
from agents import Agent, Runner, trace

load_dotenv()

agent = Agent(
    name="jokester",
    instructions="you are a joke teller",
    model="gpt-4o-mini"
)

# with trace("joke_agent_trace"): 
#     result = Runner.run_sync(starting_agent=agent, input="tell me a joke")
#     print(result.final_output) 


# The error occurs because you're using await on line 13, but the code is running at the top level 
# (not inside an async function). In Python, await can only be used within an async function.


async def joke_teller():
    result = await Runner.run(
        starting_agent=agent,
        input="tell me a joke"
    )
    print(result.final_output)  
import asyncio
asyncio.run(joke_teller())
    # print(result.final_output)
    # trace(result) 
