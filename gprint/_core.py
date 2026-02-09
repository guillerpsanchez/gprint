"""Core functionality for the gprint module."""

from __future__ import annotations

import sys
from random import choice
from typing import Optional, Sequence, Union

from ._colors import ALL_COLORS, RGBColor
from ._exceptions import InvalidRGBError

# ── ANSI escape helpers ──────────────────────────────────────────────────────

_ESC = "\033["
_RESET = f"{_ESC}0m"

# Sentinel strings for special color modes
_DEFAULT = "default"
_RANDOM = "RANDOM"


# ── Validation ───────────────────────────────────────────────────────────────


def _validate_rgb(rgb: Sequence[int]) -> RGBColor:
    """Validate and normalize an RGB color sequence.

    Args:
        rgb: A sequence of 3 integer values in the range 0-255.

    Returns:
        A validated ``(R, G, B)`` tuple.

    Raises:
        InvalidRGBError: If *rgb* is not a valid RGB specification.
    """
    if not isinstance(rgb, (list, tuple)):
        raise InvalidRGBError(
            f"RGB must be a list or tuple, got {type(rgb).__name__}"
        )
    if len(rgb) != 3:
        raise InvalidRGBError(
            f"RGB must have exactly 3 components, got {len(rgb)}"
        )
    for idx, component in enumerate(rgb):
        if not isinstance(component, int) or isinstance(component, bool):
            raise InvalidRGBError(
                f"RGB component at index {idx} must be an int, "
                f"got {type(component).__name__}"
            )
        if not 0 <= component <= 255:
            raise InvalidRGBError(
                f"RGB component at index {idx} must be 0-255, got {component}"
            )
    return (rgb[0], rgb[1], rgb[2])


# ── Color helpers ────────────────────────────────────────────────────────────


def _colorize(text: str, r: int, g: int, b: int) -> str:
    """Wrap *text* in ANSI true-color (24-bit) escape codes."""
    return f"{_ESC}38;2;{r};{g};{b}m{text}{_RESET}"


def get_random() -> RGBColor:
    """Return a random color from the built-in palette.

    Returns:
        A tuple of 3 integers ``(R, G, B)`` each in the range 0-255.

    Example::

        >>> color = get_random()
        >>> isinstance(color, tuple) and len(color) == 3
        True
    """
    return choice(ALL_COLORS)


# ── Public API ───────────────────────────────────────────────────────────────


def gprint(
    message: str,
    rgb: Union[str, Sequence[int]] = _DEFAULT,
    new_line: bool = True,
    rainbow_mode: bool = False,
    return_me: bool = False,
) -> Optional[str]:
    """Print text with RGB color support via ANSI escape codes.

    Args:
        message: The text to print.
        rgb: Color specification — one of:

            * ``"default"`` – terminal default color (no ANSI codes).
            * ``"RANDOM"``  – a random color from the built-in palette.
            * A ``(R, G, B)`` list/tuple where each value is ``0-255``.
            * Any predefined color constant (e.g. ``RED``, ``BLUE``).

        new_line: Append a newline after the message.  Defaults to ``True``.
        rainbow_mode: Print every character in a different random color.
            Defaults to ``False``.
        return_me: Return the colorized string instead of printing it.
            Useful for composing with :func:`input` or string concatenation.
            Defaults to ``False``.

    Returns:
        The colorized string when *return_me* is ``True``, otherwise ``None``.

    Raises:
        InvalidRGBError: If *rgb* is not a recognized string sentinel or a
            valid 3-component integer sequence in the 0-255 range.

    Examples::

        >>> gprint("Hello World")                            # default color
        >>> gprint("Error!", RED)                            # predefined
        >>> gprint("Custom", (255, 128, 0))                  # RGB tuple
        >>> gprint("Rainbow!", rainbow_mode=True)            # rainbow
        >>> s = gprint("Input: ", BLUE, return_me=True)      # get string
    """
    # ── Validate rgb early ───────────────────────────────────────────────
    if isinstance(rgb, str):
        if rgb not in (_DEFAULT, _RANDOM):
            raise InvalidRGBError(
                f"Unrecognized color string {rgb!r}; "
                f"expected \"default\" or \"RANDOM\""
            )
    else:
        rgb = _validate_rgb(rgb)

    # ── Rainbow mode ─────────────────────────────────────────────────────
    if rainbow_mode:
        parts = [
            _colorize(char, *get_random()) for char in message
        ]
        colored = "".join(parts)
        if return_me:
            return colored
        end = "\n" if new_line else ""
        sys.stdout.write(colored + end)
        return None

    # ── Resolve special string sentinels ─────────────────────────────────
    if rgb == _RANDOM:
        rgb = get_random()

    if rgb == _DEFAULT:
        if return_me:
            return message
        print(message, end="\n" if new_line else "")
        return None

    # ── Build and emit colored output ────────────────────────────────────
    colored = _colorize(message, rgb[0], rgb[1], rgb[2])

    if return_me:
        return colored

    print(colored, end="\n" if new_line else "")
    return None
