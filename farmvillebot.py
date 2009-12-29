import logging
import time
import mousecontrol

def class_logger(original_class):
    """Add _logger to a class"""
    original_class._logger = logging.getLogger(
        original_class.__module__ + '.' + original_class.__name__)
    return original_class


# FarmVille constants
# for zoom level 1 whatever that is
XDIST_ZOOM1 = 25
YDIST_ZOOM1 = 12


@class_logger
class FarmVilleBot(object):
    """FarmVille bot"""

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

        self._logger.info('do_action: mouse_click()')
        if not self.dry_run:
            mousecontrol.mouse_click()
        time.sleep(self.delay)

    def run(self):
        x, y = mousecontrol.get_mouse_position()
        self._logger.info('run: initial mouse position: (%d, %d)' % (x, y))
        xdist = self.zoom * XDIST_ZOOM1
        ydist = self.zoom * YDIST_ZOOM1
        xdelta = xdist
        ydelta = -ydist
        for i in range(self.nrows):
            self._logger.debug('run: i=%d' % (i, ))
            for j in range(self.ncols):
                self._logger.debug('run: j=%d' % (j, ))
                self.do_action(x, y)
                x += xdelta
                y += ydelta
            # cancel last move
            x -= xdelta
            y -= ydelta
            # next row
            x += xdist
            y += ydist
            # reverse direction
            xdelta = -xdelta
            ydelta = -ydelta
