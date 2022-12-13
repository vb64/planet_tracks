"""CLI options."""
from optparse import OptionParser

USAGE = '%prog planet_name lat lon'
VERSION = '1.0'
PARSER = OptionParser(
  usage=USAGE,
  version="%prog version {}".format(VERSION)
)
