from src.connections.wikipedia import Wikipedia


def test_wikipedia_search_for_pages():
    w = Wikipedia()

    response = w.search_for_pages("test")
    print(response)
    print()
    p = response.get('pages', [])
    for page in p:
        print(page)

if __name__ == "__main__":
    test_wikipedia_search_for_pages()
