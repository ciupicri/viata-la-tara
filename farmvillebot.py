import logging
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

