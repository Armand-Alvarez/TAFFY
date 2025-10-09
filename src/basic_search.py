import requests
import json
from enums import BASE_URLS, Sources


search_query = 'solar system'
number_of_results = 3
endpoint = 'search/page'
base_wiki_url = BASE_URLS[Sources.WIKIPEDIA]

# See https://www.mediawiki.org/wiki/API:REST_API#Client_identification
headers = {'User-Agent': 'TAFFY Searching Tool/0.1 (none)'}

url = base_wiki_url + endpoint
response = requests.get(url, headers=headers, params={'q': search_query, 'limit': number_of_results})
response = json.loads(response.text)
print(f"----\n{response}\n----")

#for page in response['pages']:
#  print(page['title'])
#  print('https://en.wikipedia.org/wiki/' + page['key'])
#  print()
