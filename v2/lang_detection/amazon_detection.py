import boto3
import json
aws_access_key_id = "AKIAVQHR43GMEWC2OO4X"
aws_secret_access_key = "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"

comprehend = boto3.client(service_name='comprehend', region_name='us-west-2', aws_access_key_id="AKIAVQHR43GMEWC2OO4X",
         aws_secret_access_key= "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")

text = "Lakkofsi sa'aa tokkoo dhihaate."

print('Calling DetectDominantLanguage')
print(json.dumps(comprehend.detect_dominant_language(Text = text), sort_keys=True, indent=4))
print("End of DetectDominantLanguage\n")