"""Module main.py tests.

make test T=test_main.py
"""
from skyfield.api import N, E, wgs84, Loader
from . import TestBase


class TestMain(TestBase):
    """Tests console client."""

    def test_args(self):
        """Call app with various args."""
        from main import main

        assert main([], self.options) == 1
        assert main(['xxx'], self.options) == 0

    def test_load(self):
        """Any tests."""
        # https://rhodesmill.org/skyfield/examples.html#at-what-angle-in-the-sky-is-the-crescent-moon
        load = Loader('skyfield-data', verbose=False)
        eph = load('de421.bsp')

        tscale = load.timescale()
        earth = eph['earth']
        point = earth + wgs84.latlon(51.551750 * N, 45.964380 * E)  # saratov

        # moon = eph['moon']
        sun = eph['sun']

        dtime = tscale.utc(2022, 12, 12, 10)
        point_at = point.at(dtime)
        elevation, azimuth, distance = point_at.observe(sun).apparent().altaz()

        print("Sun altitude: {} azimuth: {} distance: {} km".format(
          round(elevation.degrees, 6),
          round(azimuth.degrees, 6),
          int(distance.km)
        ))
