import logging
import time
import mousecontrol

# FarmVille constants
# for zoom level 1 whatever that is
XDIST_ZOOM1 = 25
YDIST_ZOOM1 = 12
XDIST_COLLECT = 6
YDIST_COLLECT = 51

def collect(bot, x, y):
    """Collect from an animal"""
    bot._logger.info('collecting...')
    bot._logger.debug('collect(%d, %d)' % (x, y))
    # activate menu
    bot._logger.debug('activating menu: mouse_click(%d, %d)' % (x, y))
    mousecontrol.mouse_click()
    time.sleep(bot.delay)
    # select menu action - collect in our case
    x += XDIST_COLLECT
    y += YDIST_COLLECT
    bot._logger.debug('selecting menu action ("Collect"): mouse_warp(%d, %d)' % (x, y))
    mousecontrol.mouse_warp(x, y)
    time.sleep(bot.delay)
    # click menu action - collect in our case
    bot._logger.debug('clicking menu action: mouse_click()')
    mousecontrol.mouse_click()

def click(bot, x, y):
    """Just do a click"""
    bot._logger.info('clicking...')
    bot._logger.debug('mouse_click()')
    mousecontrol.mouse_click()


class FarmVilleBot:
    """FarmVille bot"""
    _logger = logging.getLogger('FarmVilleBot')

    def __init__(self, nrows, ncols, dry_run, zoom, delay, action):
        self.nrows = nrows
        self.ncols = ncols
        self.dry_run = dry_run
        self.zoom = zoom
        self.delay = delay
        self.action = action

    def do_action(self, x, y):
        self._logger.info('do_action(%d, %d)' % (x, y))
        self._logger.info('mouse_warp(%d, %d)' % (x, y))
        mousecontrol.mouse_warp(x, y)
        time.sleep(self.delay)

        self.action(self, x, y)
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
