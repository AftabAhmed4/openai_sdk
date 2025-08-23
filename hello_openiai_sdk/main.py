import os
from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig,
    Agent,
    Runner
)
from dotenv import (
    load_dotenv, 
    find_dotenv
)



# Loads Environment varibles
# load_dotenv() # OpenAi
load_dotenv(find_dotenv())  # Gemini

api_key = os.getenv("GEMINI_API_KEY")
api_base_url = os.getenv("BASE_URL")


# SETUP PROVIDER

provider = AsyncOpenAI(
    api_key= api_key,
    base_url= api_base_url
)

# MODEL SETUP
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)


# CONFIG CONFIG
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# Agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful agent"
)


user_query = input("Enter Query: ")
try:
    result = Runner.run_sync(
        input=user_query,
        starting_agent=agent,
        run_config=run_config
    )
    print(result.final_output)
except Exception as e:
    print(f"Error: {str(e)}")

