from unittest.mock import Mock, patch

import pytest
from requests import RequestException

from connections.wikipedia import search_pages


@pytest.fixture
def mock_endpoint():
    with patch("connections.wikipedia.WikipediaEndpoints.search_pages") as mock:
        mock.return_value = "http://example.com/search"
        yield mock


@pytest.fixture
def mock_get():
    with patch("connections.wikipedia.requests.get") as mock:
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


class TestSearchPages:
    def test_200_status_successfully_returns_response(
        self, mock_endpoint, mock_get, mock_200_response
    ):
        mock_get.return_value = mock_200_response

        result = search_pages("test")

        assert result == {"query": "test", "results": []}
        mock_endpoint.assert_called_once_with("test")
        mock_get.assert_called_once_with("http://example.com/search")

    def test_non_200_status_code_raises_connection_error_with_string(
        self, mock_endpoint, mock_get, mock_404_response
    ):
        mock_get.return_value = mock_404_response

        expected_error_string = (
            "search_pages endpoint did not return 200. Code: 404\nerror: Not found"
        )

        with pytest.raises(
            ConnectionError,
            match=expected_error_string,
        ):
            search_pages("test")

    def test_request_exception_raises_connection_error_with_string(
        self, mock_endpoint, mock_get_with_exception_side_effect
    ):
        expected_error_string = "Failed to connect to Wikipedia API: bad request"
        with pytest.raises(ConnectionError, match=expected_error_string):
            search_pages("test")

    def test_query_gets_converted_to_string(
        self, mock_endpoint, mock_get, mock_200_response
    ):
        mock_get.return_value = mock_200_response

        search_pages(123)

        mock_endpoint.assert_called_once_with("123")
