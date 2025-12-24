from connections.constructors import WikipediaEndpoints
from connections.enums import BaseUrls


class TestWikipediaEndpoints:
    def setup_method(self):
        self.base_url = BaseUrls.WIKIPEDIA.value
        self.wikipedia_endpoints = WikipediaEndpoints()

    def test_search_pages_returns_expected_endpoint(self):
        mock_query = "test"
        result = self.wikipedia_endpoints.search_pages(mock_query)
        expected_result = self.base_url + f"/search/page?q={mock_query}"
        assert result == expected_result

    def test_get_page_returns_expected_endpoint(self):
        mock_query = "test"
        result = self.wikipedia_endpoints.get_page(mock_query)
        expected_result = self.base_url + f"/page/{mock_query}/bare"
        assert result == expected_result

    def test_get_page_with_html_returns_expected_endpoint(self):
        mock_query = "test"
        result = self.wikipedia_endpoints.get_page_with_html(mock_query)
        expected_result = self.base_url + f"/page/{mock_query}/with_html"
        assert result == expected_result
