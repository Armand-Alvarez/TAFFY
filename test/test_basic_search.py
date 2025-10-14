from basic_search import Wikipedia as Wikipedia


class TestWikipedia:
    class TestSearchForPages:
        def test_error_raised_when_non_200_status_code(self, monkeypatch):
            w = Wikipedia()
            
        
