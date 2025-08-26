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




# ================Agent
name_entity_recognition_agent = Agent(
    name="Name Entity Recognition Agent",
    instructions=(
        "You are a name entity recognition agent. "
        "You will be given multiple sentences as input. "
        "For each sentence, identify and extract all named entities such as persons, organizations, locations, dates, and other relevant entities. "
        "Return the results in a structured JSON format with the following keys: 'entities', where each entity should include 'text', 'type', and 'position' (start and end indices in the sentence). "
        "Do not include any explanation, only return the JSON object."
    )
)



async def main():
    user_input = input("Enter Query: ")
    try:
        result = await Runner.run(
            input=user_input,
            starting_agent=name_entity_recognition_agent,
            run_config=run_config
        )
        print("Final Result: ", result.final_output)
    except Exception as e:
        print("Error: ", str(e))


asyncio.run(main())