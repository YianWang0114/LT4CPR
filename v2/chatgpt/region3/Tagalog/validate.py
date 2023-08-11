import os
import openai
import argparse
import pdb
import json
from tqdm import tqdm

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-06-01-preview"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

parser = argparse.ArgumentParser()
parser.add_argument("--count", "-c", type=int, help="filename")
parser.add_argument("--session", "-s", type=int, help="session")
args = parser.parse_args()

if not os.path.exists("verification"):
  os.makedirs("verification")
lines = open(str(args.count) + '.txt').readlines()
output = []
input = ''
for l in lines[10*(args.session-1):10*args.session]:
  input += l

prompt = '''I have 10 sentences. Can you tell me the language of each? You should answer the languague name only.
            If a sentence belong to multiple lanaguges, you can write it as L1/L2 where L1, L2 are two languages. The 10 sentences are:\n {}
            '''.format(input)
response = openai.ChatCompletion.create(
engine="turbo35",
messages=[{"role": "user", "content": prompt}],
temperature=0,
max_tokens=100,
top_p=0.5,
frequency_penalty=0,
presence_penalty=0,
stop=None)
 
with open('verification/{}.txt'.format(args.count), "a") as f:
  f.writelines(response["choices"][0]["message"]["content"]+'\n')
