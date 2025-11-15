import pytest


@pytest.fixture
def sample_wiki_page_search_response():
    resp = {
        "pages": [
            {
                "id": 11089416,
                "key": "Test",
                "title": "Test",
                "excerpt": 'Look up <span class="searchmatch">test</span>, <span class="searchmatch">testing</span>, <span class="searchmatch">Test</span>, or <span class="searchmatch">TEST</span> in Wiktionary, the free dictionary. <span class="searchmatch">Test</span>(s), <span class="searchmatch">testing</span>, or <span class="searchmatch">TEST</span> may refer to: <span class="searchmatch">Test</span> (assessment), an educational assessment',
                "matched_title": None,
                "anchor": None,
                "description": "Topics referred to by the same term",
                "thumbnail": None,
            },
            {
                "id": 2249147,
                "key": ".test",
                "title": ".test",
                "excerpt": '.<span class="searchmatch">test</span> is a reserved top-level domain used to <span class="searchmatch">test</span> websites or web applications as an alternative to <span class="searchmatch">testing</span> webpages using the default localhost. It is',
                "matched_title": None,
                "anchor": None,
                "description": "Reserved domain name",
                "thumbnail": None,
            },
            {
                "id": 1858823,
                "key": "This_Is_Not_a_Test!",
                "title": "This Is Not a Test!",
                "excerpt": 'This Is Not a <span class="searchmatch">Test</span>! is the fifth studio album by American rapper Missy Elliott, released by The Goldmind Inc. and Elektra Records on November 25, 2003',
                "matched_title": None,
                "anchor": None,
                "description": "2003 studio album by Missy Elliott",
                "thumbnail": None,
            },
        ]
    }

    return resp
