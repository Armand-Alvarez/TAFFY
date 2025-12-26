from unittest.mock import patch

from typer.testing import CliRunner

from src.cli import app

runner = CliRunner()


def test_wikipedia_search_pages():
    with patch("src.cli.search_pages") as mock_search:
        mock_search.return_value = "Search results"
        result = runner.invoke(app, ["test query", "search_pages"])
        assert result.exit_code == 0
        mock_search.assert_called_once_with("test query")


def test_wikipedia_get_page():
    with patch("src.cli.get_page") as mock_get:
        mock_get.return_value = "Page metadata"
        result = runner.invoke(app, ["test query", "get_page"])
        assert result.exit_code == 0
        mock_get.assert_called_once_with("test query")


def test_wikipedia_get_page_with_html_default():
    with patch("src.cli.get_page_with_html") as mock_get_html:
        mock_get_html.return_value = "Page with HTML"
        result = runner.invoke(app, ["test query"])
        assert result.exit_code == 0
        mock_get_html.assert_called_once_with("test query")


def test_wikipedia_get_page_with_html_explicit():
    with patch("src.cli.get_page_with_html") as mock_get_html:
        mock_get_html.return_value = "Page with HTML"
        result = runner.invoke(app, ["test query", "get_page_with_html"])
        assert result.exit_code == 0
        mock_get_html.assert_called_once_with("test query")


def test_wikipedia_connection_error():
    with patch("src.cli.get_page_with_html") as mock_get_html:
        mock_get_html.side_effect = ConnectionError("Network error")
        result = runner.invoke(app, ["test query"])
        assert result.exit_code == 1
        assert "Connection Error" in result.stdout


def test_wikipedia_unknown_error():
    with patch("src.cli.get_page_with_html") as mock_get_html:
        mock_get_html.side_effect = ValueError("Unexpected error")
        result = runner.invoke(app, ["test query"])
        assert result.exit_code == 1
        assert "Unknown Error" in result.stdout
