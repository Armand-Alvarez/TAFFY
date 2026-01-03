import pytest

from connections.enums import Headers
from connections.wikipedia import get_page, get_page_with_html, search_pages

headers = Headers.WIKIPEDIA.value


class TestSearchPages:
    def test_200_status_successfully_returns_response(
        self,
        mock_search_endpoint,
        mock_get_200_status,
    ):
        result = search_pages("test")

        expected_url = "http://example.com/search&limit=3"
        expected_headers = headers

        assert result == {"query": "test", "results": []}
        mock_search_endpoint.assert_called_once_with("test")
        mock_get_200_status.assert_called_once_with(
            expected_url, headers=expected_headers
        )

    def test_non_200_status_code_raises_connection_error_with_string(
        self,
        mock_search_endpoint,
        mock_get_404_status,
    ):
        expected_error_string = (
            "search_pages endpoint did not return 200. Code: 404\nerror: Not found"
        )

        with pytest.raises(
            ConnectionError,
            match=expected_error_string,
        ):
            search_pages("test")

    def test_request_exception_raises_connection_error_with_string(
        self,
        mock_search_endpoint,
        mock_get_with_exception_side_effect,
    ):
        expected_error_string = "Failed to connect to Wikipedia API: bad request"
        with pytest.raises(ConnectionError, match=expected_error_string):
            search_pages("test")

    def test_query_gets_converted_to_string(
        self,
        mock_search_endpoint,
        mock_get_200_status,
    ):
        search_pages(123)

        mock_search_endpoint.assert_called_once_with("123")


class TestGetPage:
    def test_200_status_successfully_returns_response(
        self,
        mock_get_page_endpoint,
        mock_get_200_status,
    ):
        result = get_page("test")

        expected_url = "http://example.com/get_page"
        expected_headers = headers

        assert result == {"query": "test", "results": []}
        mock_get_page_endpoint.assert_called_once_with("test")
        mock_get_200_status.assert_called_once_with(
            expected_url, headers=expected_headers
        )

    def test_non_200_status_code_raises_connection_error_with_string(
        self,
        mock_get_page_endpoint,
        mock_get_404_status,
    ):
        expected_error_string = (
            "get_page endpoint did not return 200. Code: 404\nerror: Not found"
        )

        with pytest.raises(
            ConnectionError,
            match=expected_error_string,
        ):
            get_page("test")

    def test_request_exception_raises_connection_error_with_string(
        self,
        mock_get_page_endpoint,
        mock_get_with_exception_side_effect,
    ):
        expected_error_string = "Failed to connect to Wikipedia API: bad request"
        with pytest.raises(ConnectionError, match=expected_error_string):
            get_page("test")

    def test_query_gets_converted_to_string(
        self,
        mock_get_page_endpoint,
        mock_get_200_status,
    ):
        get_page(123)

        mock_get_page_endpoint.assert_called_once_with("123")


class TestGetPageWithHTML:
    def test_200_status_successfully_returns_response(
        self,
        mock_get_page_with_html_endpoint,
        mock_get_200_status,
    ):
        result = get_page_with_html("test")

        expected_url = "http://example.com/get_page_with_html"
        expected_headers = headers

        assert result == {"query": "test", "results": []}
        mock_get_page_with_html_endpoint.assert_called_once_with("test")
        mock_get_200_status.assert_called_once_with(
            expected_url, headers=expected_headers
        )

    def test_non_200_status_code_raises_connection_error_with_string(
        self,
        mock_get_page_with_html_endpoint,
        mock_get_404_status,
    ):
        expected_error_string = "get_page_with_html endpoint did not return 200. Code: 404\nerror: Not found"

        with pytest.raises(
            ConnectionError,
            match=expected_error_string,
        ):
            get_page_with_html("test")

    def test_request_exception_raises_connection_error_with_string(
        self,
        mock_get_page_with_html_endpoint,
        mock_get_with_exception_side_effect,
    ):
        expected_error_string = "Failed to connect to Wikipedia API: bad request"
        with pytest.raises(ConnectionError, match=expected_error_string):
            get_page_with_html("test")

    def test_query_gets_converted_to_string(
        self,
        mock_get_page_with_html_endpoint,
        mock_get_200_status,
    ):
        get_page_with_html(123)

        mock_get_page_with_html_endpoint.assert_called_once_with("123")
