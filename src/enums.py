from enum import Enum


class Sources(Enum):
    WIKIPEDIA = "wikipedia"

class API_INFORMATION(Enum):
    BASE_URL = "base_url"
    ENDPOINT = "endpoint"
    HEADERS = "headers"


API_VERSIONS = {
    Sources.WIKIPEDIA: "1",
}

CONNECTION_INFORMATION = {
    Sources.WIKIPEDIA: {
        API_INFORMATION.BASE_URL: f"https://en.wikipedia.org/w/rest.php/v{API_VERSIONS[Sources.WIKIPEDIA]}/",
        API_INFORMATION.ENDPOINT: 'search/page',
        API_INFORMATION.HEADERS: {
            'User-Agent': 'TAFFY Searching Tool/0.1 (none)'
        }
    }
}
