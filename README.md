# gprint

[![PyPI - Version](https://img.shields.io/pypi/v/gprint)](https://pypi.org/project/gprint)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gprint)](https://github.com/guillerpsanchez/gprint)
[![PyPI - License](https://img.shields.io/pypi/l/gprint)](https://github.com/guillerpsanchez/gprint/blob/main/LICENSE)
[![Tests](https://github.com/guillerpsanchez/gprint/actions/workflows/gprint-tests.yml/badge.svg)](https://github.com/guillerpsanchez/gprint/actions/workflows/gprint-tests.yml)
[![CodeQL](https://github.com/guillerpsanchez/gprint/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/guillerpsanchez/gprint/actions/workflows/codeql-analysis.yml)
[![Codecov](https://codecov.io/gh/guillerpsanchez/gprint/branch/main/graph/badge.svg)](https://codecov.io/gh/guillerpsanchez/gprint)
[![Maintainer](https://img.shields.io/badge/maintainer-guillerpsanchez-blue)](https://github.com/guillerpsanchez)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/guillerpsanchez/gprint/graphs/commit-activity)

**gprint** is a lightweight Python module that allows you to print colored text on almost any terminal using RGB color codes.

## Features

- 🎨 **Full RGB Support**: Use any RGB color (0-255 for each channel)
- 🌈 **Rainbow Mode**: Print each character with a random color
- 📦 **175+ Predefined Colors**: Use color constants like RED, BLUE, GREEN, etc.
- 🚀 **Lightweight**: No external dependencies
- ✅ **100% Test Coverage**: Thoroughly tested with 22 unit tests
- 🐍 **Modern Python Support**: Compatible with Python 3.8 through 3.13
- 🔒 **Type Safe**: Comprehensive error handling for invalid inputs

## Installation

```bash
pip install gprint
```

## Compatibility and Testing

gprint is actively maintained and tested on Python 3.8, 3.9, 3.10, 3.11, 3.12, and 3.13.

Our comprehensive CI/CD pipeline runs 22 tests across all supported Python versions on every push, ensuring 100% code coverage and reliability. We use:

- **Automated Testing**: GitHub Actions runs tests on every commit
- **Security Scanning**: CodeQL analyzes code for vulnerabilities weekly
- **Dependency Management**: Dependabot keeps dependencies up-to-date
- **Quality Checks**: Linting and formatting validation

## Quick Start

```python
from gprint import gprint, RED, BLUE, GREEN

# Basic colored text
gprint("Hello, World!", rgb=RED)

# Using RGB values
gprint("Custom color!", rgb=[100, 200, 255])

# Rainbow mode
gprint("Colorful text!", rainbow_mode=True)

# Return colored string instead of printing
colored_text = gprint("Input: ", rgb=BLUE, new_line=False, return_me=True)
user_input = input(colored_text)
```

## API Reference

### `gprint(message, rgb="default", new_line=True, rainbow_mode=False, return_me=False)`

**Parameters:**

- **`message`** (str): The text to be printed or returned
- **`rgb`** (list | str, optional): Color specification. Can be:
  - A list of 3 integers `[R, G, B]` where each value is 0-255
  - A predefined color constant (e.g., `RED`, `BLUE`, `GREEN`)
  - `"RANDOM"` for a random color from the palette
  - `"default"` for terminal's default color
  - Default: `"default"`
- **`new_line`** (bool, optional): Whether to add a newline after the text. Default: `True`
- **`rainbow_mode`** (bool, optional): Print each character with a random color. Default: `False`
- **`return_me`** (bool, optional): Return the colored string instead of printing. Default: `False`

**Returns:**
- `str` if `return_me=True`, otherwise `None`

**Raises:**
- `InvalidRGBError`: If RGB values are invalid (not 3 values, out of 0-255 range)

### `get_random()`

Returns a random color from the predefined color palette.

**Returns:**
- `list`: A list of 3 strings representing RGB values

## Examples

### Basic Usage

```python
from gprint import gprint

# Simple colored text
gprint("Success!", rgb=[0, 255, 0])  # Green
gprint("Error!", rgb=[255, 0, 0])    # Red
gprint("Warning!", rgb=[255, 255, 0]) # Yellow
```

### Using Color Constants

```python
from gprint import gprint, RED, GREEN, BLUE, ORANGE, PURPLE

gprint("This is red", rgb=RED)
gprint("This is green", rgb=GREEN)
gprint("This is blue", rgb=BLUE)
gprint("This is orange", rgb=ORANGE)
gprint("This is purple", rgb=PURPLE)
```

### Rainbow Mode

```python
from gprint import gprint

gprint("Every character gets a different color!", rainbow_mode=True)
```

### Without Newline

```python
from gprint import gprint, BLUE, GREEN

gprint("Question: ", rgb=BLUE, new_line=False)
gprint("Answer", rgb=GREEN)
```

### Return Instead of Print

```python
from gprint import gprint, RED, GREEN

# Use with input()
prompt = gprint("Enter your name: ", rgb=GREEN, new_line=False, return_me=True)
name = input(prompt)

# Build colored strings
success = gprint("✓ Success", rgb=GREEN, return_me=True)
error = gprint("✗ Error", rgb=RED, return_me=True)
print(f"Status: {success if True else error}")
```

### Random Colors

```python
from gprint import gprint, get_random

# Random color from palette
gprint("Surprise color!", rgb="RANDOM")

# Get random color value
my_color = get_random()
gprint("Using the same random color", rgb=my_color)
gprint("Still the same color", rgb=my_color)
```

### Error Handling

```python
from gprint import gprint, InvalidRGBError

try:
    gprint("Invalid color", rgb=[256, 0, 0])  # Out of range
except InvalidRGBError as e:
    print(f"Error: {e}")

try:
    gprint("Invalid color", rgb=[255, 0])  # Wrong length
except InvalidRGBError as e:
    print(f"Error: {e}")
```

## Available Colors

gprint includes 175+ predefined color constants. Here are some examples:

**Reds:** RED, DARK_RED, CRIMSON, TOMATO, CORAL, SALMON
**Oranges:** ORANGE, DARK_ORANGE, ORANGE_RED, GOLD
**Yellows:** YELLOW, KHAKI, LEMON_CHIFFON
**Greens:** GREEN, LIME, FOREST_GREEN, SEA_GREEN, OLIVE
**Blues:** BLUE, NAVY, SKY_BLUE, STEEL_BLUE, TURQUOISE
**Purples:** PURPLE, VIOLET, MAGENTA, ORCHID, INDIGO
**Browns:** BROWN, SIENNA, CHOCOLATE, PERU, TAN
**Grays:** GRAY, SILVER, DIM_GRAY, LIGHT_GRAY
**Special:** BLACK, WHITE, PINK, BEIGE

See the full list in `gprint/gprint.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/guillerpsanchez/gprint.git
cd gprint

# Install development dependencies
pip install -r requirements.txt
pip install ruff black isort

# Run tests
pytest --cov=gprint --cov-report=term-missing

# Run linting
ruff check gprint/
black --check gprint/
isort --check-only gprint/
```

## Security

If you discover a security vulnerability, please send an email to [guillermo@guillerpsanchez.dev](mailto:guillermo@guillerpsanchez.dev). All security vulnerabilities will be promptly addressed.

See [SECURITY.md](SECURITY.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📧 **Email**: guillermo@guillerpsanchez.dev
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/guillerpsanchez/gprint/issues)
- 💬 **Questions**: [GitHub Discussions](https://github.com/guillerpsanchez/gprint/discussions)

## Acknowledgments

- Thanks to all contributors who have helped improve gprint
- Inspired by the need for simple, cross-platform colored terminal output

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

> 0.0.7  
    - Fixed error if a string is provided in rgb.  
    - Added error handling. 

> 0.0.8  
    - Updated and checked compatibility with python 3.10   

> 0.0.9  
    - Updated test  
    - Updated compability with Python 3.11  
