import pytest
from unittest.mock import patch, mock_open, MagicMock
import sys


class TestAITools:
    @patch.dict("sys.modules", {"google": MagicMock(), "google.genai": MagicMock()})
    @patch("src.ai_tools.os.makedirs")
    @patch("builtins.open", new_callable=mock_open, read_data="test cv content")
    @patch("src.ai_tools.os.getenv")
    def test_cv_cleaner(self, mock_getenv, mock_file, mock_makedirs):
        mock_getenv.return_value = "test_api_key"

        # Import after patching
        from src.ai_tools import cv_cleaner

        # Mock the genai module that was imported
        import src.ai_tools

        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "formatted cv content"
        mock_client.models.generate_content.return_value = mock_response
        src.ai_tools.genai.Client.return_value = mock_client

        result = cv_cleaner("test_cv.md")

        assert result == "formatted cv content"
        mock_makedirs.assert_called_with("userdata/processed cv", exist_ok=True)

    @patch.dict("sys.modules", {"google": MagicMock(), "google.genai": MagicMock()})
    @patch("src.ai_tools.os.makedirs")
    @patch("builtins.open", new_callable=mock_open, read_data="test cv content")
    @patch("src.ai_tools.os.getenv")
    def test_cv_analyser(self, mock_getenv, mock_file, mock_makedirs):
        mock_getenv.return_value = "test_api_key"

        from src.ai_tools import cv_analyser

        import src.ai_tools

        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "cv analysis result"
        mock_client.models.generate_content.return_value = mock_response
        src.ai_tools.genai.Client.return_value = mock_client

        result = cv_analyser("test_cv.md")

        assert result == "cv analysis result"
        mock_makedirs.assert_called_with("userdata/ai_analysis", exist_ok=True)

    @patch.dict("sys.modules", {"google": MagicMock(), "google.genai": MagicMock()})
    @patch("src.ai_tools.os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    @patch("src.ai_tools.os.getenv")
    def test_cv_scorer(self, mock_getenv, mock_file, mock_makedirs):
        mock_getenv.return_value = "test_api_key"

        from src.ai_tools import cv_scorer

        import src.ai_tools

        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "54 out of 75"
        mock_client.models.generate_content.return_value = mock_response
        src.ai_tools.genai.Client.return_value = mock_client

        mock_file.return_value.read.side_effect = ["test cv content", "test rubric"]

        with patch("builtins.print"):
            result = cv_scorer("test_cv.md")

        assert result == "54 out of 75"
        mock_makedirs.assert_called_with("userdata/ai_analysis", exist_ok=True)
