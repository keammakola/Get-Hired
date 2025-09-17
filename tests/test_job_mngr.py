import unittest
from unittest.mock import patch
from src.job_mngr import scrape_web

class TestScrapeWeb(unittest.TestCase):
    @patch('builtins.input', return_value='https://google.com')
    @patch('src.job_mngr.requests.get')
    @patch('src.job_mngr.BeautifulSoup')
    def test_scrape_web(self, mock_beautifulsoup, mock_requests_get, mock_input):
        # Mock the requests.get method to return a predefined response
        mock_response = 'Mocked response content'
        mock_requests_get.return_value.content = mock_response.encode('utf-8')

        # Mock the BeautifulSoup method to return a predefined BeautifulSoup object
        mock_beautifulsoup.return_value.get_text.return_value = 'Mocked page text'

        # Call the scrape_web function
        scrape_web()

        # Assert that the file has been written correctly
        with open('userdata/jobs/job_page.txt', 'r') as f:
            self.assertEqual(f.read(), 'Mocked page text')

if __name__ == '__main__':
    unittest.main()