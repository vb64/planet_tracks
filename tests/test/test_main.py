"""Module main.py tests.

make test T=test_main.py
"""
from datetime import datetime, timezone
from skyfield.api import wgs84, Loader
from . import TestBase


class TestMain(TestBase):
    """Tests console client."""

    # saratov
    sar_lat = 51.551750
    sar_lon = 45.964380

    def test_args(self):
        """Call app with various args."""
        import main

        assert main.main([], self.options) == 1

        saved = main.make_loops
        main.make_loops = lambda location, planet, start, tscale, length, step, border: []
        assert main.main(['sun', str(self.sar_lat), str(self.sar_lon)], self.options) == 0
        main.make_loops = saved

    def test_make_loops(self):
        """Function make_loops."""
        import main

        load = Loader('skyfield-data', verbose=False)
        eph = load('de421.bsp')
        location = eph['earth'] + wgs84.latlon(self.sar_lat, self.sar_lon)

        loops = main.make_loops(
          location, eph['sun'],
          datetime(2022, 12, 12, 10).replace(tzinfo=timezone.utc),
          load.timescale(),
          60 * 60 * 24 * 2,
          60 * 30,
          10
        )
        assert len(loops) == 2
        assert main.dump_loops(loops) is None
