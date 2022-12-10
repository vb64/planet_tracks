"""CLI options."""
from optparse import OptionParser

USAGE = '%prog lat lon planet_name'
VERSION = '1.0'
PARSER = OptionParser(
  usage=USAGE,
  version="%prog version {}".format(VERSION)
)
