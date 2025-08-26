import os 
from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig,
    Agent,
    Runner
)

from dotenv import(
    load_dotenv,
    find_dotenv
)

from openai.types.responses import ResponseTextDeltaEvent

import asyncio

# loads envoriment varaibales
load_dotenv(find_dotenv())  # Gemini

api_key = os.getenv("GEMINI_API_KEY")
api_base_url = os.getenv("BASE_URL")
#=============== prvider saart


if not api_key:
    raise Exception("GEMINI_API_KEY is not set in environment variables")
if not api_base_url:
    raise Exception("BASE_URL is not set in environment variables")

provider = AsyncOpenAI(
    api_key=api_key,
    base_url=api_base_url
)

#=====================prvider end 

#====================== modal sart 
model  =OpenAIChatCompletionsModel(
    model ="gemini-2.0-flash",
    openai_client=provider
)
#++++++++++++++++++++++++++++ modal end
#========================= config sart 
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)






# ============================ Agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful agent"
)



async def main():
    user_input = input("Enter: ")
    result = Runner.run_streamed(
        input = user_input,
        starting_agent=agent,
        run_config=run_config
    )

    async for chunk in result.stream_events():
        if chunk.type == "raw_response_event" and isinstance(chunk.data, ResponseTextDeltaEvent):
            print(chunk.data.delta, end="", flush=True)


asyncio.run(main())