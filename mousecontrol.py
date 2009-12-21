#
# Based on code from http://ubuntuforums.org/showpost.php?p=4862593&postcount=7
#
import Xlib.display
import Xlib.ext.xtest

_display = Xlib.display.Display()
_screen = _display.screen()
_root = _screen.root

def mouse_click(button):
    """button = 1 left, 2 middle, 3 right"""
    mouse_down(button)
    mouse_up(button)

def mouse_down(button): 
    Xlib.ext.xtest.fake_input(_display, Xlib.X.ButtonPress, button)
    _display.sync()

def mouse_up(button):
    Xlib.ext.xtest.fake_input(_display, Xlib.X.ButtonRelease, button)
    _display.sync()

def mouse_warp(x, y):
    _root.warp_pointer(x, y)
    _display.sync()

def get_mouse_position():
    """get_mouse_position() -> x, y"""
    d = _root.query_pointer()._data
    return d['root_x'], d['root_y']

def get_screen_resolution():
    return _screen['width_in_pixels'], _screen['height_in_pixels']
