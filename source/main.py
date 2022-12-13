"""Console client."""
import sys
from datetime import datetime, timedelta, timezone
from skyfield.api import Loader, wgs84
from cli_options import PARSER, VERSION

COPYRIGHTS = '(C) by Vitaly Bogomolov 2022'
OPTS = None

LAT = 51.551750
LON = 45.964380
PLANET = 'sun'

STEP = 20  # seconds
MIN_ELEVATION = 1.0  # degree
LENGTH = 60 * 60 * 24 * 5  # 5 days
START = datetime(2022, 12, 12).replace(tzinfo=timezone.utc)


def make_loops(location, planet, start, tscale, length, step, border):
    """Create data for given location and planet."""
    loops = []
    loop = None

    for i in range(int(length / step)):
        ptime = tscale.from_datetime(start + timedelta(seconds=i * step))
        elevation, azimuth,  *_ = location.at(ptime).observe(planet).apparent().altaz()
        if elevation.degrees < border:
            if loop:
                loops.append(loop)
                loop = None
            continue

        if loop is None:
            loop = []

        loop.append((ptime, elevation, azimuth))

    return loops


def dump_loops(loops):
    """Dump loops data."""
    for loop in loops:
        for ptime, elevation, azimuth in loop:
            print(
              ptime.astimezone(timezone.utc),
              round(azimuth.degrees, 6),
              round(elevation.degrees, 6),
            )
        print()


def main(argv, _options):
    """Entry point."""
    print("Planet tracks utility v.{}. {}".format(VERSION, COPYRIGHTS))
    if not argv:
        PARSER.print_usage()
        return 1

    # https://rhodesmill.org/skyfield/examples.html#at-what-angle-in-the-sky-is-the-crescent-moon
    load = Loader('skyfield-data', verbose=False)
    eph = load('de421.bsp')
    location = eph['earth'] + wgs84.latlon(LAT, LON)  # saratov
    start = START

    print(PLANET, 'from', start)
    dump_loops(make_loops(location, eph[PLANET], start, load.timescale(), LENGTH, STEP, MIN_ELEVATION))

    return 0


if __name__ == '__main__':  # pragma: no cover
    OPTS, ARGS = PARSER.parse_args()
    sys.exit(main(ARGS, OPTS))
