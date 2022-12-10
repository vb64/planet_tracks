"""Console client."""
import sys
from cli_options import PARSER, VERSION

COPYRIGHTS = '(C) by Vitaly Bogomolov 2022'
OPTS = None


def main(argv, _options):
    """Entry point."""
    print("Planet tracks utility v.{}. {}".format(VERSION, COPYRIGHTS))
    if not argv:
        PARSER.print_usage()
        return 1

    return 0


if __name__ == '__main__':  # pragma: no cover
    OPTS, ARGS = PARSER.parse_args()
    sys.exit(main(ARGS, OPTS))
