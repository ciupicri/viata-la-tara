#!/usr/bin/env python
import logging
from optparse import OptionParser
import sys
import time

import mousecontrol

# FarmVille constants
# for zoom level 1 whatever that is
XDIST = 25
YDIST = 12

class FarmVilleBot:
    """FarmVille bot"""
    _logger = logging.getLogger('FarmVilleBot')

    def __init__(self, nrows, ncols, dry_run, zoom, delay):
        self.nrows = nrows
        self.ncols = ncols
        self.dry_run = dry_run
        self.zoom = zoom
        self.delay = delay

    def do_action(self, x, y):
        self._logger.info('do_action: mouse_warp(%d, %d)' % (x, y))
        if not self.dry_run:
            mousecontrol.mouse_warp(x, y)
        time.sleep(self.delay)

        self._logger.info('do_action: mouse_click(1)')
        if not self.dry_run:
            mousecontrol.mouse_click(1)
        time.sleep(self.delay)

    def run(self):
        x, y = mousecontrol.get_mouse_position()
        self._logger.info('run: initial mouse position: (%d, %d)' % (x, y))
        xdelta = self.zoom * XDIST
        ydelta = self.zoom * YDIST
        for i in range(self.nrows):
            self._logger.debug('run: i=%d' % (i, ))
            for j in range(self.ncols):
                self._logger.debug('run: j=%d' % (j, ))
                self.do_action(x, y)
                x += xdelta
            x -= xdelta # cancel last move
            xdelta = -xdelta # reverse direction
            y += ydelta

def parse_options():
    parser = OptionParser()
    parser.set_defaults(dry_run=False, zoom=1, delay=0.5, log_level=logging.WARN)
    parser.add_option('-n', '--dry-run',
                      action='store_true', dest='dry_run',
                      help="""Don't actually run any commands; just print them.""")
    parser.add_option('-z', '--zoom',
                      type='int', dest='zoom',
                      help='zoom level: 1 - 4')
    parser.add_option('--delay',
                      type='float', dest='delay',
                      help='delay between mouse actions')
    parser.add_option('-v', '--verbose',
                      action='store_const', const=logging.INFO, dest='log_level',
                      help='set logging level to INFO')
    parser.add_option('--debug',
                      action='store_const', const=logging.DEBUG, dest='log_level',
                      help='set logging level to DEBUG')
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
