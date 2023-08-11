import os
import openai
import argparse
import pdb
import json

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-06-01-preview"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

parser = argparse.ArgumentParser()
parser.add_argument("--language", "-l", type=str, help="Language you want to extract from LLM")
parser.add_argument("--count", "-c", type=int, help="Number of times the experiment is conducted")
args = parser.parse_args()
 

response = openai.Completion.create(

  engine="turbo35",

  prompt="Could you please write me 100 sentences in {}?".format(args.language),

  temperature=0,

  max_tokens=3000,

  top_p=0.5,

  frequency_penalty=0,

  presence_penalty=0,

  #best_of=1,

  stop=None)

print(response)
if not os.path.exists("raw_output/{}".format(args.language)):
    os.makedirs("raw_output/{}".format(args.language))

json_file_path = "raw_output/{}/{}.json".format(args.language, args.count)
response_json = json.dumps(response, indent=4)
with open(json_file_path, "w") as json_file:
    json_file.write(response_json)

