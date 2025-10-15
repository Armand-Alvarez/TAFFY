import requests
import pytest
from src.connections.wikipedia import Wikipedia


w = Wikipedia()

@pytest.mark.parametrize("status_code", [400, 401, 402, 500, 501, 502])
def test_raise_error_on_non_200_response(monkeypatch, mock_get, status_code):
    mock_request_get = mock_get(status_code=status_code)
    monkeypatch.setattr(requests, "get", mock_request_get)

    with pytest.raises(ConnectionError):
        w.search_for_pages()
