import pytest

from connections.wikipedia import search_pages


class TestSearchPages:
    def test_200_status_successfully_returns_response(
        self,
        mock_endpoint,
        mock_get_200_status,
    ):
        result = search_pages("test")

        assert result == {"query": "test", "results": []}
        mock_endpoint.assert_called_once_with("test")
        mock_get_200_status.assert_called_once_with("http://example.com/search")

    def test_non_200_status_code_raises_connection_error_with_string(
        self,
        mock_endpoint,
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
        self, mock_endpoint, mock_get_with_exception_side_effect,
    ):
        expected_error_string = "Failed to connect to Wikipedia API: bad request"
        with pytest.raises(ConnectionError, match=expected_error_string):
            search_pages("test")

    def test_query_gets_converted_to_string(
        self,
        mock_endpoint,
        mock_get_200_status,
    ):
        search_pages(123)

        mock_endpoint.assert_called_once_with("123")
