"""Module main.py tests.

make test T=test_main.py
"""
from . import TestBase


class TestMain(TestBase):
    """Tests console client."""

    def test_args(self):
        """Call app with various args."""
        from main import main

        assert main([], self.options) == 1
        assert main(['xxx'], self.options) == 0
