import mousecontrol
import time
import util

# FarmVille constants
XDIST_ZOOM1 = 25 # for zoom level 1
YDIST_ZOOM1 = 12 # for zoom level 1
YDIST_MENU_ITEM = 22 # y distance between menu items

@util.class_logger
class FarmVilleBot(object):
    """FarmVille Bot"""

    def __init__(self, zoom, delay, step):
        self.x, self.y = mousecontrol.get_mouse_position()
        self._logger.info("__init__: x = %s, y = %s" % (self.x, self.y))
        self._logger.info("__init__: zoom = %s, delay = %s, step = %s" %
                          (zoom, delay, step))
        self.zoom = zoom
        self.delay = delay
        self.step = step

    # movement

    def move(self, ysteps, xsteps):
        """Move bot with ysteps on vertical and xsteps on horizontal"""
        self._logger.info("move(%s, %s)" % (ysteps, xsteps))
        # move with ysteps
        self.x += ysteps * self.step * self.zoom * XDIST_ZOOM1
        self.y -= ysteps * self.step * self.zoom * YDIST_ZOOM1
        # move with xsteps
        self.x += xsteps * self.step * self.zoom * XDIST_ZOOM1
        self.y += xsteps * self.step * self.zoom * YDIST_ZOOM1
        self._logger.debug("move: mouse_warp(%s, %s)" % (self.x, self.y))
        mousecontrol.mouse_warp(self.x, self.y)
        time.sleep(self.delay)

    def up(self):
        return self.move(1, 0)

    def down(self):
        return self.move(-1, 0)

    def left(self):
        return self.move(0, -1)

    def right(self):
        return self.move(0, 1)

    # simple actions

    def click(self):
        self._logger.info("click")
        mousecontrol.mouse_click()
        time.sleep(self.delay)

    def menu_action(self, action):
        """action = 1 (first menu item), 2 (second menu item), ..."""
        self._logger.info("menu_action(%d)" % (action, ))
        mousecontrol.mouse_click()
        time.sleep(self.delay)
        mousecontrol.mouse_warp(self.x + 5,
                                self.y + 5 + (action-1) * YDIST_MENU_ITEM)
        mousecontrol.mouse_click()
        time.sleep(self.delay)

    def collect(self):
        self._logger.info("collect")
        self.menu_action(3)
