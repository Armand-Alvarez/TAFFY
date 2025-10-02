import requests
import json


query = input("Enter your query")
url = f"https://en.wikipedia.org/wiki/{query}"

response = requests.get(url)
print(response)
