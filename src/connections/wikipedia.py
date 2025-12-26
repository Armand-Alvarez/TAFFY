import requests

from connections.constructors import WikipediaEndpoints

headers = {
    "User-Agent": "TAFFY: Terminal Answer Finder For You! Project at (github.com/Armand-Alvarez/TAFFY)"
}
limit = 3


def search_pages(query: str) -> dict:
    """
    Hit the search_pages Wikipedia API endpoint. Return the response JSON as a dict if 200 status code.

    Args:
        query (str): The page to search.
    Returns:
        dict: The JSON response converted to dict. Only returns on 200.
    Raises:
        ConnectionError: If non-200 status code or if get request fails.
    """
    query = str(query)
    endpoint = WikipediaEndpoints().search_pages(query) + f"&limit={limit}"
    try:
        resp = requests.get(endpoint, headers=headers)
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to Wikipedia API: {e}")

    if resp.status_code == 200:
        return resp.json()
    else:
        raise ConnectionError(
            f"search_pages endpoint did not return 200. Code: {resp.status_code}\nerror: {resp.text}"
        )


def get_page(query: str) -> dict:
    """
    Hit the get_page Wikipedia API endpoint. Return the response JSON as a dict if 200 status code.

    Args:
        query (str): The page to get.
    Returns:
        dict: The JSON response converted to dict. Only returns on 200.
    Raises:
        ConnectionError: If non-200 status code or if get request fails.
    """
    query = str(query)
    endpoint = WikipediaEndpoints().get_page(query)
    try:
        resp = requests.get(endpoint, headers=headers)
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to Wikipedia API: {e}")

    if resp.status_code == 200:
        return resp.json()
    else:
        raise ConnectionError(
            f"get_page endpoint did not return 200. Code: {resp.status_code}\nerror: {resp.text}"
        )


def get_page_with_html(query: str) -> dict:
    """
    Hit the get_page_with_html Wikipedia API endpoint. Return the response JSON as a dict if 200 status code.

    Args:
        query (str): The page to get.
    Returns:
        dict: The JSON response converted to dict. Only returns on 200.
    Raises:
        ConnectionError: If non-200 status code or if get request fails.
    """
    query = str(query)
    endpoint = WikipediaEndpoints().get_page_with_html(query)
    headers = {
        "User-Agent": "TAFFY terminal search engine. Docs: github.com/Armand-Alvarez/TAFFY"
    }
    try:
        resp = requests.get(endpoint, headers=headers)
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to Wikipedia API: {e}")
    if resp.status_code == 200:
        return resp.json()
    else:
        raise ConnectionError(
            f"get_page_with_html endpoint did not return 200. Code: {resp.status_code}\nerror: {resp.text}"
        )
