import pytest

@pytest.fixture
def mock_requests_get():
    def _make_mock(status_code, text="Mocked response"):
        class MockResponse:
            def __init__(self):
                self.status_code = status_code
                self.text = text

        def mock_get(*args, **kwargs):
            return MockResponse()

        return mock_get

    return _make_mock
