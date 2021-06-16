# gprint

[![PyPI - License](https://img.shields.io/pypi/l/gprint)](https://github.com/guillerpsanchez/gprint/blob/main/LICENSE)
[![Mantainer](https://img.shields.io/badge/maintainer-guillerpsanchez-blue)](https://github.com/guillerpsanchez)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/guillerpsanchez/gprint)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gprint)](https://github.com/guillerpsanchez/gprint)
[![PyPI](https://img.shields.io/pypi/v/gprint)](https://pypi.org/project/gprint)

gprint is a Python module that allows to print color on almost any terminal.


## How to import

```python
from gprint import *
```

## Usage

```python
gprint(message, rgb, new_line, rainbow_mode, return_me)
```
message         = String with the text to be printed.

rgb             = A list of 3 Integers from 0 to 255 that represents every color on rgb scale, a color code (RED, BLUE....) can be used too. Defaults to "default" (white text).

new_line        = A boolean that represents if you want a new line after the printed text or not. Defaults to True.

rainbow_mode    = A boolean that allows the command to print every character from a pseudo-randomized color. Defaults to False.

return_me       = A boolean that allows to return of the colorized text instead of printing it directly (useful for other commands like input() ). Defaults to False.

## Errors and contact

> guillermo@guillerpsanchez.dev

Feel free to contact me at any time.

## Changelog

> 0.0.1  
    - Initial release.

> 0.0.2  
    - Added rainbow_mode.  
    - Added new_line.

> 0.0.3  
    - Fixed problem with randomized colors.  
    - Added return_me.

> 0.0.4  
    - Fixed problem with rainbow_mode, now it should work with new_line.  
    - Fixed problem with "RANDOM" string as color, nowit should work faster and with other flags.  
    - Added new function to get random color, the program now should work faster.

> 0.0.5  
    - Updated code with better syntax.  
    - Now runs faster than ever.

> 0.0.6  
    - Fixed bug with new line on rainbow mode.  