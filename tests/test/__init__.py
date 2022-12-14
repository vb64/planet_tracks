"""Root class for testing."""
import os
from unittest import TestCase

BUILD_DIR = 'build'


class TestBase(TestCase):
    """Base class for tests."""

    def setUp(self):
        """Set up tests."""
        super().setUp()

        from cli_options import PARSER
        self.options, _args = PARSER.parse_args(args=[])
        self.lat = "51.588843"
        self.lon = "45.962577"

        if not os.path.isdir(BUILD_DIR):
            os.mkdir(BUILD_DIR)

    @staticmethod
    def build(file_name):
        """Return path to file in 'build' folder."""
        return os.path.join(BUILD_DIR, file_name)
