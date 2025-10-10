import requests
from enums import Sources, CONNECTION_INFORMATION, API_INFORMATION
import json


search_query = 'solar system'
number_of_results = 3
wiki_conn_info = CONNECTION_INFORMATION[Sources.WIKIPEDIA]
url = wiki_conn_info[API_INFORMATION.BASE_URL] + wiki_conn_info[API_INFORMATION.ENDPOINT]
headers = wiki_conn_info[API_INFORMATION.HEADERS]

response = requests.get(url, headers=headers, params={'q': search_query, 'limit': number_of_results})
response = json.loads(response.text)
pages = response["pages"]
for page in pages:
    print(page["title"])
