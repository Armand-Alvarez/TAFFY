from enum import Enum


class BaseUrls(Enum):
    WIKIPEDIA = "https://en.wikipedia.org/w/rest.php/v1"


class WikipediaEndpoints(Enum):
    SEARCH_PAGES = f"{BaseUrls.WIKIPEDIA.value}/search/page"
    GET_PAGE = f"{BaseUrls.WIKIPEDIA}//page/{0}/bare"
    GET_PAGE_WITH_HTML = (
        lambda user_value: f"{BaseUrls.WIKIPEDIA}/page/{user_value}/with_html"
    )
