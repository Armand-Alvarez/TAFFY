from typing import Annotated

import typer
from rich import print

from connections.wikipedia import get_page, get_page_with_html, search_pages
from enums import WikipediaQueryTypes

app = typer.Typer()


@app.command()
def wikipedia(
    query: Annotated[str, typer.Argument(help="The query to search for.")],
    type: Annotated[
        WikipediaQueryTypes, typer.Argument(help="The type of Wikipedia query to make.")
    ] = WikipediaQueryTypes.GET_PAGE_WITH_HTML,
) -> None:
    """
    Make a query to Wikipedia.

    Args:
        query (str): The string to query
        type (search_pages | get_page | get_page_with_html):
            search_pages = search for a page by title
            get_page = get metadata for an article
            get_page_with_html (default) = Get an article
    """
    if type == WikipediaQueryTypes.SEARCH_PAGES:
        fn = search_pages
    elif type == WikipediaQueryTypes.GET_PAGE:
        fn = get_page
    else:
        fn = get_page_with_html

    try:
        resp = fn(query)
    except ConnectionError as e:
        print(f"[bold red]❗Connection Error:[/bold red] {e}")
        raise typer.Exit(1)
    except Exception as e:
        print(f"[bold red]❗Unknown Error:[/bold red] {e}")
        raise typer.Exit(1)

    print(resp)


if __name__ == "__main__":
    app()
