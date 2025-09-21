import pytest
from unittest.mock import patch, mock_open, MagicMock
from src.job_mngr import scrape_web, paste_to_text


class TestJobManager:
    @patch("src.job_mngr.os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    @patch("src.job_mngr.BeautifulSoup")
    @patch("src.job_mngr.requests.get")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_scrape_web(
        self, mock_print, mock_input, mock_get, mock_soup, mock_file, mock_makedirs
    ):
        mock_input.return_value = "https://example.com/job"
        mock_response = MagicMock()
        mock_response.content = "<html>job content</html>"
        mock_get.return_value = mock_response

        mock_soup_instance = MagicMock()
        mock_soup_instance.get_text.return_value = "extracted job text"
        mock_soup.return_value = mock_soup_instance

        scrape_web()

        mock_get.assert_called_with("https://example.com/job")
        mock_makedirs.assert_called_with("userdata/jobs", exist_ok=True)
        mock_file.assert_called_with("userdata/jobs/job_page.txt", "w")
        mock_file().write.assert_called_with("extracted job text")

    @patch("src.job_mngr.os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input")
    @patch("builtins.print")
    def test_paste_to_text(self, mock_print, mock_input, mock_file, mock_makedirs):
        mock_input.return_value = "pasted job information"

        paste_to_text()

        mock_makedirs.assert_called_with("userdata/jobs", exist_ok=True)
        mock_file.assert_called_with("userdata/jobs/job_page.txt", "w")
        mock_file().write.assert_called_with("pasted job information")
