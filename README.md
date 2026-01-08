# gprint

[![PyPI - License](https://img.shields.io/pypi/l/gprint)](https://github.com/guillerpsanchez/gprint/blob/main/LICENSE)
[![Maintainer](https://img.shields.io/badge/maintainer-guillerpsanchez-blue)](https://github.com/guillerpsanchez)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/guillerpsanchez/gprint)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gprint)](https://github.com/guillerpsanchez/gprint)
[![PyPI](https://img.shields.io/pypi/v/gprint)](https://pypi.org/project/gprint)

gprint is a Python module that allows you to print colored text on almost any terminal.

## Installation

```bash
pip install gprint
```

## Compatibility

gprint supports Python 3.8 through 3.13. Compatibility is verified through automated testing using GitHub Actions on each push to the main branch.

## Quick Start

```python
from gprint import *

# Basic usage - default color
gprint("Hello World!")

# Using a predefined color
gprint("This is red!", RED)
gprint("This is blue!", BLUE)

# Using custom RGB values
gprint("Custom orange!", [255, 165, 0])

# Rainbow mode - each character in a random color
gprint("Rainbow text!", rainbow_mode=True)

# Random color
gprint("Random color!", "RANDOM")

# No newline at the end
gprint("Same line... ", new_line=False)
gprint("continues here!")

# Return colored string instead of printing (useful for input())
name = input(gprint("Enter your name: ", CYAN, return_me=True))
```

## API Reference

### `gprint(message, rgb, new_line, rainbow_mode, return_me)`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | str | required | The text to be printed |
| `rgb` | list/str | `"default"` | Color specification (see below) |
| `new_line` | bool | `True` | Print newline after the message |
| `rainbow_mode` | bool | `False` | Print each character in a random color |
| `return_me` | bool | `False` | Return the string instead of printing |

#### Color Options (`rgb` parameter)

- `"default"` - Uses terminal default color
- `"RANDOM"` - Uses a random color from the palette
- `[R, G, B]` - List of 3 integers (0-255) for custom colors
- Predefined constants - See available colors below

### `get_random()`

Returns a random color from the available color palette as an RGB list.

```python
color = get_random()  # Returns something like [255, 0, 0]
```

## Available Colors

### Basic Colors
`RED`, `GREEN`, `BLUE`, `YELLOW`, `CYAN`, `MAGENTA`, `WHITE`, `BLACK`

### Reds & Pinks
`MAROON`, `DARK_RED`, `BROWN`, `FIREBRICK`, `CRIMSON`, `TOMATO`, `CORAL`, `INDIAN_RED`, `LIGHT_CORAL`, `DARK_SALMON`, `SALMON`, `LIGHT_SALMON`, `ORANGE_RED`, `DEEP_PINK`, `HOT_PINK`, `LIGHT_PINK`, `PINK`

### Oranges & Yellows
`DARK_ORANGE`, `ORANGE`, `GOLD`, `DARK_GOLDEN_ROD`, `GOLDEN_ROD`, `PALE_GOLDEN_ROD`, `DARK_KHAKI`, `KHAKI`, `OLIVE`, `LEMON_CHIFFON`, `LIGHT_YELLOW`

### Greens
`DARK_GREEN`, `FOREST_GREEN`, `LIME`, `LIME_GREEN`, `LIGHT_GREEN`, `PALE_GREEN`, `DARK_SEA_GREEN`, `MEDIUM_SPRING_GREEN`, `SPRING_GREEN`, `SEA_GREEN`, `MEDIUM_SEA_GREEN`, `OLIVE_DRAB`, `DARK_OLIVE_GREEN`, `YELLOW_GREEN`, `GREEN_YELLOW`, `LAWN_GREEN`, `CHART_REUSE`

### Blues & Cyans
`NAVY`, `DARK_BLUE`, `MEDIUM_BLUE`, `ROYAL_BLUE`, `DODGER_BLUE`, `DEEP_SKY_BLUE`, `SKY_BLUE`, `LIGHT_SKY_BLUE`, `LIGHT_BLUE`, `POWDER_BLUE`, `STEEL_BLUE`, `CORN_FLOWER_BLUE`, `CADET_BLUE`, `MIDNIGHT_BLUE`, `TEAL`, `DARK_CYAN`, `AQUA`, `LIGHT_CYAN`, `DARK_TURQUOISE`, `TURQUOISE`, `MEDIUM_TURQUOISE`, `PALE_TURQUOISE`, `AQUA_MARINE`, `LIGHT_SEA_GREEN`

### Purples & Violets
`INDIGO`, `PURPLE`, `DARK_MAGENTA`, `DARK_VIOLET`, `DARK_ORCHID`, `MEDIUM_ORCHID`, `BLUE_VIOLET`, `MEDIUM_PURPLE`, `DARK_SLATE_BLUE`, `SLATE_BLUE`, `MEDIUM_SLATE_BLUE`, `THISTLE`, `PLUM`, `VIOLET`, `ORCHID`, `FUCHSIA`, `MEDIUM_VIOLET_RED`, `PALE_VIOLET_RED`

### Neutrals & Grays
`GAINSBORO`, `LIGHT_GRAY`, `SILVER`, `DARK_GRAY`, `GRAY`, `DIM_GRAY`, `LIGHT_SLATE_GRAY`, `SLATE_GRAY`, `DARK_SLATE_GRAY`, `WHITE_SMOKE`, `SNOW`, `GHOST_WHITE`

### Browns & Earth Tones
`SADDLE_BROWN`, `SIENNA`, `CHOCOLATE`, `PERU`, `SANDY_BROWN`, `BURLY_WOOD`, `TAN`, `ROSY_BROWN`, `MOCCASIN`, `NAVAJO_WHITE`, `PEACH_PUFF`, `BISQUE`, `BLANCHED_ALMOND`, `WHEAT`, `CORN_SILK`, `ANTIQUE_WHITE`, `BEIGE`

### Other Colors
`HONEYDEW`, `MINT_CREAM`, `AZURE`, `ALICE_BLUE`, `LAVENDER`, `LAVENDER_BLUSH`, `MISTY_ROSE`, `LINEN`, `OLD_LACE`, `PAPAYA_WHIP`, `SEA_SHELL`, `FLORAL_WHITE`, `IVORY`

## Errors and Contact

> guillermo@guillerpsanchez.dev

Feel free to contact me at any time.

## Changelog

> 0.1.0
- Major code refactoring and cleanup
- Fixed bug where `rgb="RANDOM"` was not working correctly
- Fixed duplicate `ORANGE` color definition
- Fixed incorrect `PURE_RED_LIGHT_*` color values
- Changed RGB values from strings to integers for consistency
- Added type hints and improved docstrings
- Improved test coverage with pytest
- Updated GitHub Actions to v4/v5
- Dropped support for Python 3.5, 3.6, and 3.7 (end of life)
- Added support for Python 3.12 and 3.13
- Updated to use PyPI Trusted Publishers for releases

> 0.0.9
- Updated tests
- Updated compatibility with Python 3.11

> 0.0.8
- Updated and checked compatibility with Python 3.10

> 0.0.7
- Fixed error if a string is provided in rgb
- Added error handling

> 0.0.6
- Fixed bug with new line on rainbow mode

> 0.0.5
- Updated code with better syntax
- Now runs faster than ever

> 0.0.4
- Fixed problem with rainbow_mode, now it should work with new_line
- Fixed problem with "RANDOM" string as color, now it should work faster and with other flags
- Added new function to get random color, the program now should work faster

> 0.0.3
- Fixed problem with randomized colors
- Added return_me

> 0.0.2
- Added rainbow_mode
- Added new_line

> 0.0.1
- Initial release
