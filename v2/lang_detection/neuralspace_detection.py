AUTHORIZATION_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI1OTIyNDgzLCJkYXRhIjp7ImVtYWlsIjoid2FuZ3lpYW5AdXcuZWR1Iiwicm9sZSI6InByb3ZpZGVyIiwiYXBpa2V5IjoiMmRmODRkMTAtMzkwNS00ZTE1LTkyZDgtNTc1OTUwNzAyNjFjIiwicmVmZXJlbmNlS2V5IjoiMmRmODRkMTAtMzkwNS00ZTE1LTkyZDgtNTc1OTUwNzAyNjFjIiwicGxhblR5cGUiOiJkZWZhdWx0IiwiY291bnRyeSI6IlVuaXRlZCBTdGF0ZXMifSwiaWF0IjoxNjkyNTkxODg4fQ.4qlSvWXZxWpNGJ8BS5wUzvpatjLEtCs1e2Ukn5YMZQk"
#Get all supported language
curl --location --request GET 'https://platform.neuralspace.ai/api/language-detection/v1/supported-languages' \
--header "Authorization: ${AUTHORIZATION_TOKEN}"

# Detect language
curl --location --request POST 'https://platform.neuralspace.ai/api/language-detection/v1/detect' \
--header 'Accept: application/json, text/plain, */*' \
--header "authorization: ${AUTHORIZATION_TOKEN}" \
--header 'Content-Type: application/json;charset=UTF-8' \
--data-raw '{
    "text": "An ginkakarawat ko nga feedback gikan ha imo gin-aapreciate ko ngan gin-aconsider ha akon decisions."
}'


