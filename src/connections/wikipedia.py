import requests

from connections.constructors import WikipediaEndpoints


def search_pages(query: str) -> dict:
    query = str(query)
    endpoint = WikipediaEndpoints.search_pages(query)
    try:
        resp = requests.get(endpoint)
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to Wikipedia API: {e}")

    if resp.status_code == 200:
        return resp.json()
    else:
        raise ConnectionError(
            f"search_pages endpoint did not return 200. Code: {resp.status_code}\nerror: {resp.text}"
        )
