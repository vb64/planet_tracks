"""Console client."""
import sys
from skyfield.api import Loader
from cli_options import PARSER, VERSION

COPYRIGHTS = '(C) by Vitaly Bogomolov 2022'
OPTS = None


def main(argv, _options):
    """Entry point."""
    print("Planet tracks utility v.{}. {}".format(VERSION, COPYRIGHTS))
    if not argv:
        PARSER.print_usage()
        return 1

    load = Loader('skyfield-data', verbose=False)
    eph = load('de421.bsp')
    print(eph['Sun'])

    return 0


if __name__ == '__main__':  # pragma: no cover
    OPTS, ARGS = PARSER.parse_args()
    sys.exit(main(ARGS, OPTS))
