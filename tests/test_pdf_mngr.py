import pytest
from unittest.mock import patch, mock_open, MagicMock
from src.pdf_mngr import parse_pdf


class TestPDFManager:
    @patch("src.pdf_mngr.os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    @patch("src.pdf_mngr.PdfReader")
    @patch("src.pdf_mngr.os.path.exists")
    @patch("builtins.input")
    def test_parse_pdf_success(
        self, mock_input, mock_exists, mock_reader, mock_file, mock_makedirs
    ):
        mock_input.return_value = "test.pdf"
        mock_exists.return_value = True

        mock_page = MagicMock()
        mock_page.extract_text.return_value = "extracted text"
        mock_reader_instance = MagicMock()
        mock_reader_instance.pages = [mock_page]
        mock_reader.return_value = mock_reader_instance

        parse_pdf()

        mock_makedirs.assert_called_once()
        mock_file.assert_called()

    @patch("builtins.print")
    @patch("src.pdf_mngr.os.path.exists")
    @patch("builtins.input")
    def test_parse_pdf_file_not_found(self, mock_input, mock_exists, mock_print):
        mock_input.return_value = "nonexistent.pdf"
        mock_exists.return_value = False

        parse_pdf()

        mock_print.assert_called_with("Error: File does not exist")

    @patch("builtins.print")
    @patch("src.pdf_mngr.PdfReader")
    @patch("src.pdf_mngr.os.path.exists")
    @patch("builtins.input")
    def test_parse_pdf_reader_exception(
        self, mock_input, mock_exists, mock_reader, mock_print
    ):
        mock_input.return_value = "test.pdf"
        mock_exists.return_value = True
        mock_reader.side_effect = Exception("PDF parsing error")

        parse_pdf()

        # Check that some error was printed (the exact message may vary)
        assert mock_print.called
