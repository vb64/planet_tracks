"""CLI options."""
from optparse import OptionParser

USAGE = '%prog planet_name lat lon'
VERSION = '1.0'
PARSER = OptionParser(
  usage=USAGE,
  version="%prog version {}".format(VERSION)
)

PARSER.add_option(
  "--step",
  type="int",
  dest="step",
  default=20,
  help="Track points step in seconds. Default is 20"
)
PARSER.add_option(
  "--length",
  type="int",
  dest="length",
  default=60 * 60 * 24 * 5,  # 5 days
  help="Track length in seconds. Default is 432000 (5 days)."
)
PARSER.add_option(
  "--min_elevation",
  type="float",
  dest="min_elevation",
  default=1,
  help="Minimal planet elevation in degrees above horizon. Default is 1."
)
