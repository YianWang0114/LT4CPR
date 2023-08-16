import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import pdb
from random import sample
import argparse

key = "0e027c33aa7e41948ea3a2992606a15c"
endpoint = "https://azurelang.cognitiveservices.azure.com/"

parser = argparse.ArgumentParser()
parser.add_argument("--filename", "-f", type=str, help="file's relative directory")
parser.add_argument("--number", "-n", type=int, help="number", default=10)
args = parser.parse_args()

def read_sentences():
    lines = open(args.filename).readlines()
    samples = sample(lines, args.number)
    return samples

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for detecting the language of text
def language_detection_example(client, sentence):
    try:
        documents = [sentence] #Input can be one sentence or a document with multiple sentences
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        #print("Language: ", response.primary_language.name)
        return response.primary_language.name

    except Exception as err:
        print("Encountered exception. {}".format(err))

samples = read_sentences()
result = []
for i in samples:
    pred = language_detection_example(client, i)
    result.append(pred)

print(result)

