import requests
from src.enums import Sources, CONNECTION_INFORMATION, API_INFORMATION, API_FUNCTIONS
import json


class Wikipedia:
    wiki_conn_info = CONNECTION_INFORMATION[Sources.WIKIPEDIA]

    def search_for_pages(self, query: str = "", number_of_results: int =3) -> dict:
        """
        Searches for the most releveant (n) wikipedia page titles and returns the titles as a list (where n is Wikipedia.number_of_results)

        Args:
            query (str): The query to search for
            number_of_results (int): The number of page titles you want to receive (Defaults to 3)
                
        Returns:
            dict: The json response
        """
        url = self.wiki_conn_info[API_FUNCTIONS.SEARCH_PAGES][API_INFORMATION.BASE_URL] + self.wiki_conn_info[API_FUNCTIONS.SEARCH_PAGES][API_INFORMATION.ENDPOINT]
        headers = self.wiki_conn_info[API_FUNCTIONS.SEARCH_PAGES][API_INFORMATION.HEADERS]

        params = self.wiki_conn_info[API_FUNCTIONS.SEARCH_PAGES][API_INFORMATION.PARAMS]
        params['q'] = params['q'].format(query=query)
        params['limit'] = params['limit'].format(number_of_results=number_of_results)

        try:
            response = requests.get(url=url, headers=headers, params=params)
            response.raise_for_status()
            response = json.loads(response.text)
            return(response)
        except requests.exceptions.RequestException:
            raise ConnectionError
