import os

if 'DISPLAY' in os.environ:
    from .x11 import *
else:
    from .win32 import *
