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

    def __init__(self, zoom, delay):
        self.x, self.y = mousecontrol.get_mouse_position()
        self.zoom = zoom
        self.delay = delay

    # movement

    def move(self, nrows, ncols):
        self._logger.info("move(%s, %s)" % (nrows, ncols))
        # move with nrows
        self.x += nrows * self.zoom * XDIST_ZOOM1
        self.y -= nrows * self.zoom * YDIST_ZOOM1
        # move with ncols
        self.x += ncols * self.zoom * XDIST_ZOOM1
        self.y += ncols * self.zoom * YDIST_ZOOM1
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
