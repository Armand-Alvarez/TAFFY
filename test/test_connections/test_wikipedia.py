import requests
import pytest
from src.connections.wikipedia import Wikipedia


w = Wikipedia()

class TestWikipedia:
    @pytest.mark.parametrize("status_code", [400, 401, 402, 500, 501, 502])
    def test_raise_error_on_non_200_response(self, monkeypatch, mock_get, status_code):
        mock_request_get = mock_get(status_code=status_code)
        monkeypatch.setattr(requests, "get", mock_request_get)

        with pytest.raises(ConnectionError):
            w.search_for_pages()


    def test_search_for_pages_returns_expected_response(self, monkeypatch, mock_get, sample_wiki_page_search_response):
        mock_request_get = mock_get(status_code=200, json_data=sample_wiki_page_search_response)
        monkeypatch.setattr(requests, "get", mock_request_get)

        response = w.search_for_pages("test", number_of_results=3)
        assert response == sample_wiki_page_search_response
