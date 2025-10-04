from enum import Enum


class Sources(Enum):
    WIKIPEDIA = "wikipedia"


API_VERSIONS = {
    Sources.WIKIPEDIA: "1",
    }
