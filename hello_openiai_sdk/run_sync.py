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

# =============== Loads ENV Var Start
load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")
api_base_url = os.getenv("BASE_URL")

# =============== Loads ENV Var End


# =============== 1. provider start
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=api_base_url
)
# =============== provider end


# =============== 2. modal start
modal = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)
# =============== modal end


# =============== 3. config start
run_config = RunConfig(
    model=modal,
    model_provider=provider,
    tracing_disabled=True
)
# =============== config end


# ===============================================================  AGENT  ==================================================================
text_classification_agent = Agent(
    name="Text Classification Agent",
    instructions=(
        "You are a sentiment analysis agent. "
        "You will be given multiple user comments as input. "
        "For each comment, classify it strictly as either 'Positive' or 'Negative'. "
        "At the end, return a summary in JSON with the following keys: "
        "'positive_count', 'negative_count', 'positive_percentage', 'negative_percentage'. "
        "Do not include any explanation, only return the JSON object."
    )
)





user_input = """
This product is amazing!
I hate the packaging.
Fast delivery, very happy.
Worst experience ever.
I Love the Coding.
I hate manager behaviour.
I hate heavy traffic
"""



try:
    result = Runner.run_sync(
        input=user_input,
        starting_agent=text_classification_agent,
        run_config=run_config
    )

    print("Final Result: ", result.final_output)
except Exception as e:
    print("Error: ", str(e))
