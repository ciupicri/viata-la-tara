=============
FarmVille bot
=============

A bot for the FarmVille_ game. It works on both X11 (Unix/Linux) and Windows.

.. _FarmVille: http://www.farmville.com

Requirements
============

Unix/Linux (X11)
----------------

It uses the X11 XTEST extension to control the mouse, so you will need to
install ``python-xlib``.

Windows
-------

It uses the AutoIt_ COM to control the mouse. You will need to install the
following:

- Python_ 2.6 or later for Windows
- `Python win32 extensions`_
- AutoIt_

.. _AutoIt: http://www.autoitscript.com/autoit3
.. _Python: http://www.python.org/download/
.. _Python win32 extensions: http://sourceforge.net/projects/pywin32/


Usage
=====

To harvest, plow or plant an area of 7 rows x 10 columns:

``./main.py --debug --zoom 1 --delay 0.7 7 10``

To collect from the animals or harvest the trees from an area of 3 rows and 8 columns:

``./main.py --debug --zoom 1 --delay 0.7 --collect 3 8``

A screencast_ is also available.

.. _screencast: http://www.youtube.com/watch?v=iUpa2_8lZVg
