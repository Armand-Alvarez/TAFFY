import requests
from enums import BASE_URLS, Sources
import json


search_query = 'solar system'
number_of_results = 3
endpoint = 'search/page'
base_wiki_url = BASE_URLS[Sources.WIKIPEDIA]

# See https://www.mediawiki.org/wiki/API:REST_API#Client_identification
headers = {'User-Agent': 'TAFFY Searching Tool/0.1 (none)'}

url = base_wiki_url + endpoint
response = requests.get(url, headers=headers, params={'q': search_query, 'limit': number_of_results})
response = json.loads(response.text)
pages = response["pages"]
for page in pages:
    print(page["title"])
