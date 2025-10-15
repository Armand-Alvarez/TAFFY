import pytest
import requests

class MockResponse:
    def __init__(self, status_code=200, json_data=None, text=None):
        self.status_code = status_code
        self._json_data = json_data or {"pages": [{"title": "Mock Page"}]}
        self._text = text or "test text"

    def json(self):
        return self._json_data

    def text(self):
        return self._text

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError(f"Status code: {self.status_code}")

@pytest.fixture
def mock_get():
    def _mock_get(status_code=200, json_data=None, text=None):
        def _request(*args, **kwargs):
            return MockResponse(status_code=status_code, json_data=json_data)
        return _request
    return _mock_get
