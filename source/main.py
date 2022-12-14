"""Console client."""
import sys
import csv
from datetime import datetime, timedelta, timezone
from skyfield.api import Loader, wgs84
from cli_options import PARSER, VERSION

COPYRIGHTS = '(C) by Vitaly Bogomolov 2022'
OPTS = None
DATE_MASK = '%Y-%m-%d:%H:%M'


def make_loops(location, planet, start, tscale, length, step, border):
    """Create data for given location and planet."""
    loops = []
    loop = None

    for i in range(int(length / step)):
        ptime = tscale.from_datetime(start + timedelta(seconds=i * step))
        elevation, azimuth, *_ = location.at(ptime).observe(planet).apparent().altaz()
        if elevation.degrees < border:
            if loop:  # pragma: no branch
                loops.append(loop)
                loop = None
            continue

        if loop is None:
            loop = []

        loop.append((ptime, elevation, azimuth))

    return loops


def dump_loops(out_file, loops, title):
    """Dump loops data to csv."""
    with open(out_file, 'w', encoding='utf-8') as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        writer.writerow([title])
        writer.writerow(['Time, UTC', 'Azimuth, degrees', 'Elevation, degrees'])

        for loop in loops:
            for ptime, elevation, azimuth in loop:
                writer.writerow([
                  ptime.astimezone(timezone.utc),
                  round(azimuth.degrees, 6),
                  round(elevation.degrees, 6),
                ])
            writer.writerow([])


def main(argv, options):
    """Entry point."""
    print("Planet tracks utility v.{}. {}".format(VERSION, COPYRIGHTS))
    if len(argv) != 3:
        PARSER.print_usage()
        return 1

    # https://rhodesmill.org/skyfield/examples.html#at-what-angle-in-the-sky-is-the-crescent-moon
    load = Loader('skyfield-data', verbose=False)
    eph = load('de421.bsp')
    location = eph['earth'] + wgs84.latlon(float(argv[1]), float(argv[2]))

    start = datetime.utcnow()
    if options.utcnow:
        start = datetime.strptime(options.utcnow, DATE_MASK)
    start = start.replace(tzinfo=timezone.utc)

    out_file = "{}_{}_{}.csv".format(
      argv[0],
      start.strftime(DATE_MASK),
      (start + timedelta(seconds=options.length)).strftime(DATE_MASK)
    ).replace(':', '-')
    if options.output:
        out_file = options.output

    print('Processing...')
    loops = make_loops(
      location,
      eph[argv[0]],
      start,
      load.timescale(),
      options.length,
      options.step,
      options.min_elevation
    )

    print('Saving to {}...'.format(out_file))
    dump_loops(out_file, loops, "{} from {}".format(argv[0], start))
    print('Done.')

    return 0


if __name__ == '__main__':  # pragma: no cover
    OPTS, ARGS = PARSER.parse_args()
    sys.exit(main(ARGS, OPTS))
