crop_statusbar.py
==================

This is a simple python script to batch crop status bars from iOS screenshots.

While current support is limited to Retina iPhone size images, additional resolutions can be easily added by extending `crop_size(image)`.


Prerequisites
-------------

pngcrush: `brew install pngcrush`

PIL/Pillow: `pip3 install Pillow`


Usage
-----

`crop_statusbar.py *.png`


License
-------

© 2013 Masaru Itoh / Masmor

Released under the [MIT License][*1].

[*1]: http://opensource.org/licenses/MIT