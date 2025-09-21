import pytest
from unittest.mock import patch
from src.user_details import basic_info


class TestUserDetails:
    @patch("builtins.print")
    @patch("builtins.input")
    def test_basic_info(self, mock_input, mock_print):
        mock_input.return_value = "John Doe"

        basic_info()

        mock_input.assert_called_with("Enter your First name & Surname: ")
        assert mock_print.call_count == 2
        mock_print.assert_any_call("John")
        mock_print.assert_any_call("Doe")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_basic_info_single_name(self, mock_input, mock_print):
        mock_input.return_value = "John"

        with pytest.raises(ValueError):
            basic_info()
