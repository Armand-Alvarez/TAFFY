from enum import Enum


class Sources(Enum):
    WIKIPEDIA = "wikipedia"


API_VERSIONS = {
    Sources.WIKIPEDIA: "1",
}

BASE_URLS = {
    Sources.WIKIPEDIA: f"https://en.wikipedia.org/w/rest.php/v{API_VERSIONS[Sources.WIKIPEDIA]}/",
}
