from enum import Enum


class BaseUrls(Enum):
    WIKIPEDIA = "https://en.wikipedia.org/w/rest.php/v1"


class Headers(Enum):
    WIKIPEDIA = {
        "User-Agent": "TAFFY: Terminal Answer Finder For You! Project at (github.com/Armand-Alvarez/TAFFY)"
    }


class Limits(Enum):
    WIKIPEDIA = 3
