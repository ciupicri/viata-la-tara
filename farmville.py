#!/usr/bin/env python
import logging
from optparse import OptionParser

from farmvillebot import FarmVilleBot

def parse_options():
    parser = OptionParser()
    parser.set_defaults(dry_run=False, zoom=4, delay=0.5, log_level=logging.WARN)
    parser.add_option('-n', '--dry-run',
                      action='store_true', dest='dry_run',
                      help="""don't actually run any commands; just print them.""")
    parser.add_option('-z', '--zoom',
                      type='int', dest='zoom',
                      help="zoom level: 1 - 4")
    parser.add_option('--delay',
                      type='float', dest='delay',
                      help="delay between mouse actions")
    parser.add_option('-v', '--verbose',
                      action='store_const', const=logging.INFO, dest='log_level',
                      help="set logging level to INFO")
    parser.add_option('--debug',
                      action='store_const', const=logging.DEBUG, dest='log_level',
                      help="set logging level to DEBUG")
    return parser.parse_args()

def main():
    options, args = parse_options()
    nrows, ncols = (int(x) for x in args)
    logging.basicConfig(level=options.log_level)
    bot = FarmVilleBot(nrows, ncols,
                       options.dry_run, options.zoom, options.delay)
    bot.run()

if __name__ == '__main__':
    main()
