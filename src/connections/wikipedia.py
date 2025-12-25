import requests

from connections.constructors import WikipediaEndpoints


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
    endpoint = WikipediaEndpoints.get_page(query)
    try:
        resp = requests.get(endpoint)
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
    endpoint = WikipediaEndpoints.get_page_with_html(query)
    try:
        resp = requests.get(endpoint)
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to Wikipedia API: {e}")
    if resp.status_code == 200:
        return resp.json()
    else:
        raise ConnectionError(
            f"get_page_with_html endpoint did not return 200. Code: {resp.status_code}\nerror: {resp.text}"
        )
