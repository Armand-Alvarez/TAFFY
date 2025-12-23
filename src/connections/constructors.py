from enums import BaseUrls


class WikipediaEndpoints:
    def __init__(self):
        self.base = BaseUrls.WIKIPEDIA.value

    def search_pages(self, query: str) -> str:
        """
        Construct endpoint for wikipedia search_pages endpoint

        Args:
                query (str): The query to search

        Returns:
        str: The constructed endpoint
        """

        endpoint = f"/search/page?q={query}"

        return self.base + endpoint

    def get_page(self, query: str) -> str:
        """
        Construct endpoint for wikipedia get_page endpoint

        Args:
                query (str): The query to search

        Returns:
                str: The constructed endpoint
        """

        endpoint = f"/page/{query}/bare"

        return self.base + endpoint

    def get_page_with_html(self, query: str) -> str:
        """
        Construct endpoint for wikipedia get_page_with_html endpoint

        Args:
                query (str): The query to search

        Returns:
                str: The constructed endpoint
        """

        endpoint = f"/page/{query}/with_html"

        return self.base + endpoint
