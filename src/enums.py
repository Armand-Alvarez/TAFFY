from enum import Enum


class Sources(Enum):
    WIKIPEDIA = "wikipedia"

class API_INFORMATION(Enum):
    BASE_URL = "base_url"
    ENDPOINT = "endpoint"
    HEADERS = "headers"
    URL = "url"
    PARAMS = "params"

class API_FUNCTIONS(Enum):
    SEARCH_PAGES = "search_pages"
    GET_PAGE = "get_page"

API_VERSIONS = {
    Sources.WIKIPEDIA: "1",
}

CONNECTION_INFORMATION = {
    Sources.WIKIPEDIA: {
        API_FUNCTIONS.SEARCH_PAGES: {
            API_INFORMATION.BASE_URL: f"https://en.wikipedia.org/w/rest.php/v{API_VERSIONS[Sources.WIKIPEDIA]}/",
            API_INFORMATION.ENDPOINT: 'search/page',
            API_INFORMATION.HEADERS: {
                'User-Agent': 'TAFFY Searching Tool/0.1 (none)'
            },
            API_INFORMATION.PARAMS: {'q': '{query}', 'limit': '{number_of_results}'}
        },
        API_FUNCTIONS.GET_PAGE: {
            API_INFORMATION.BASE_URL: f"https://en.wikipedia.org/w/rest.php/v{API_VERSIONS[Sources.WIKIPEDIA]}/",
            API_INFORMATION.ENDPOINT: 'page/{title}/with_html',
            API_INFORMATION.HEADERS: {
                'User-Agent': 'TAFFY Searching Tool/0.1 (none)'
            }
        }
    }
}
