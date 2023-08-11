import os
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

 

response = openai.Completion.create(

  engine="turbo35",

  prompt="""Could you translate the following sentence into Swahili:

A major outbreak spread around the world in 2020, leading to considerable investment and research activity to develop a vaccine.

""",

  temperature=0.9,

  max_tokens=100,

  top_p=0.5,

  frequency_penalty=0,

  presence_penalty=0,

  #best_of=1,

  stop=None)

print(response)