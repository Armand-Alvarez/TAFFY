from unittest.mock import Mock, patch

import pytest
from requests import RequestException


@pytest.fixture
def mock_endpoint():
    with patch("connections.wikipedia.WikipediaEndpoints.search_pages") as mock:
        mock.return_value = "http://example.com/search"
        yield mock


@pytest.fixture
def mock_get_200_status(mock_200_response):
    with patch("connections.wikipedia.requests.get") as mock:
        mock.return_value = mock_200_response
        yield mock


@pytest.fixture
def mock_get_404_status(mock_404_response):
    with patch("connections.wikipedia.requests.get") as mock:
        mock.return_value = mock_404_response
        yield mock



@pytest.fixture
def mock_get_with_exception_side_effect():
    with patch("connections.wikipedia.requests.get") as mock:
        mock.side_effect = RequestException("bad request")
        yield mock


@pytest.fixture
def mock_200_response():
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"query": "test", "results": []}
    return response


@pytest.fixture
def mock_404_response():
    response = Mock()
    response.status_code = 404
    response.text = "Not found"
    return response
