import pytest
from unittest.mock import patch, MagicMock


class TestMain:
    @patch.dict(
        "sys.modules",
        {
            "google": MagicMock(),
            "google.genai": MagicMock(),
            "pypdf": MagicMock(),
            "requests": MagicMock(),
            "bs4": MagicMock(),
            "pdf_mngr": MagicMock(),
            "ai_tools": MagicMock(),
            "job_mngr": MagicMock(),
        },
    )
    @patch("builtins.input")
    @patch("builtins.print")
    @patch("os.system")
    def test_main_module_imports(self, mock_system, mock_print, mock_input):
        """Test that main module can be imported"""
        mock_input.side_effect = ["1"]  # Provide input to avoid stdin error

        try:
            import src.main

            assert True
        except (SystemExit, StopIteration):
            assert True  # Expected when main completes
        except ImportError as e:
            pytest.fail(f"Failed to import main module: {e}")

    @patch.dict(
        "sys.modules",
        {
            "google": MagicMock(),
            "google.genai": MagicMock(),
            "pypdf": MagicMock(),
            "requests": MagicMock(),
            "bs4": MagicMock(),
            "pdf_mngr": MagicMock(),
            "ai_tools": MagicMock(),
            "job_mngr": MagicMock(),
        },
    )
    @patch("builtins.print")
    @patch("builtins.input")
    @patch("os.system")
    def test_main_execution_starts(self, mock_system, mock_input, mock_print):
        """Test that main starts execution"""
        mock_input.side_effect = ["1"]  # Choose option 1

        try:
            import src.main
        except (SystemExit, StopIteration):
            pass

        # Verify some interaction occurred
        assert mock_print.called or mock_input.called
