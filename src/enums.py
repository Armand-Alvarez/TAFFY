from enum import Enum

class WikipediaQueryTypes(Enum):
    SEARCH_PAGES = "search_pages"
    GET_PAGE = "get_page"
    GET_PAGE_WITH_HTML = "get_page_with_html"