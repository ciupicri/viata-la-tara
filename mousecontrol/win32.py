from win32com.client import Dispatch

_AutoIt = Dispatch("AutoItX3.Control")

def mouse_click(): # TODO: button=1
    _AutoIt.MouseClick()

def mouse_warp(x, y):
    _AutoIt.MouseMove(x, y)

def get_mouse_position():
    """get_mouse_position() -> x, y"""
    return _AutoIt.MouseGetPosX(), _AutoIt.MouseGetPosY()
