"""Tests for the gprint core functionality."""

from __future__ import annotations

import pytest

from gprint import (
    BLUE,
    RED,
    WHITE,
    GprintError,
    InvalidRGBError,
    get_random,
    gprint,
)


# ── Basic output ─────────────────────────────────────────────────────────────


class TestDefaultOutput:
    """Printing without color arguments."""

    def test_prints_with_newline(self, capsys: pytest.CaptureFixture[str]) -> None:
        gprint("Hello world")
        assert capsys.readouterr().out == "Hello world\n"

    def test_prints_without_newline(self, capsys: pytest.CaptureFixture[str]) -> None:
        gprint("Hello world", new_line=False)
        assert capsys.readouterr().out == "Hello world"

    def test_return_default_gives_plain_string(self) -> None:
        assert gprint("Hello world", return_me=True) == "Hello world"

    def test_returns_none_when_printing(self) -> None:
        assert gprint("Hello world") is None


# ── Color output ─────────────────────────────────────────────────────────────


class TestColorOutput:
    """Printing with explicit colors."""

    def test_rgb_tuple(
        self, capsys: pytest.CaptureFixture[str], ansi_prefix: str, ansi_reset: str,
    ) -> None:
        gprint("Red text", rgb=(255, 0, 0))
        out = capsys.readouterr().out
        assert out == f"{ansi_prefix}255;0;0mRed text{ansi_reset}\n"

    def test_rgb_list(
        self, capsys: pytest.CaptureFixture[str], ansi_prefix: str, ansi_reset: str,
    ) -> None:
        gprint("Red text", rgb=[255, 0, 0])
        out = capsys.readouterr().out
        assert out == f"{ansi_prefix}255;0;0mRed text{ansi_reset}\n"

    def test_predefined_red(
        self, capsys: pytest.CaptureFixture[str], ansi_prefix: str, ansi_reset: str,
    ) -> None:
        gprint("Red text", rgb=RED)
        out = capsys.readouterr().out
        assert out == f"{ansi_prefix}255;0;0mRed text{ansi_reset}\n"

    def test_predefined_blue(
        self, capsys: pytest.CaptureFixture[str], ansi_prefix: str, ansi_reset: str,
    ) -> None:
        gprint("Blue text", rgb=BLUE)
        out = capsys.readouterr().out
        assert out == f"{ansi_prefix}0;0;255mBlue text{ansi_reset}\n"

    def test_return_colored_string(self, ansi_prefix: str, ansi_reset: str) -> None:
        result = gprint("Red text", rgb=(255, 0, 0), return_me=True)
        assert result == f"{ansi_prefix}255;0;0mRed text{ansi_reset}"

    def test_colored_no_newline(
        self, capsys: pytest.CaptureFixture[str], ansi_prefix: str, ansi_reset: str,
    ) -> None:
        gprint("Red", rgb=RED, new_line=False)
        out = capsys.readouterr().out
        assert not out.endswith("\n")
        assert f"{ansi_prefix}255;0;0mRed{ansi_reset}" == out


# ── Random color ─────────────────────────────────────────────────────────────


class TestRandomColor:
    """Tests for the RANDOM sentinel and get_random()."""

    def test_random_produces_ansi(
        self, capsys: pytest.CaptureFixture[str], ansi_prefix: str, ansi_reset: str,
    ) -> None:
        gprint("Random", rgb="RANDOM")
        out = capsys.readouterr().out
        assert ansi_prefix in out
        assert ansi_reset in out

    def test_get_random_returns_valid_tuple(self) -> None:
        color = get_random()
        assert isinstance(color, tuple)
        assert len(color) == 3
        assert all(isinstance(v, int) and 0 <= v <= 255 for v in color)

    def test_get_random_varies(self) -> None:
        """get_random should not always return the same color."""
        colors = {get_random() for _ in range(50)}
        assert len(colors) > 1


# ── Rainbow mode ─────────────────────────────────────────────────────────────


class TestRainbowMode:
    """Tests for rainbow_mode."""

    def test_each_char_colored(
        self, capsys: pytest.CaptureFixture[str], ansi_prefix: str,
    ) -> None:
        gprint("ABC", rainbow_mode=True)
        out = capsys.readouterr().out
        assert out.count(ansi_prefix) == 3

    def test_rainbow_with_newline(self, capsys: pytest.CaptureFixture[str]) -> None:
        gprint("AB", rainbow_mode=True)
        assert capsys.readouterr().out.endswith("\n")

    def test_rainbow_without_newline(self, capsys: pytest.CaptureFixture[str]) -> None:
        gprint("AB", rainbow_mode=True, new_line=False)
        assert not capsys.readouterr().out.endswith("\n")

    def test_rainbow_return_me(self, ansi_prefix: str) -> None:
        result = gprint("AB", rainbow_mode=True, return_me=True)
        assert result is not None
        assert result.count(ansi_prefix) == 2

    def test_rainbow_empty_string(self, capsys: pytest.CaptureFixture[str]) -> None:
        gprint("", rainbow_mode=True)
        assert capsys.readouterr().out == "\n"


# ── Input validation ─────────────────────────────────────────────────────────


class TestValidation:
    """Tests for invalid input handling."""

    def test_too_few_components(self) -> None:
        with pytest.raises(InvalidRGBError, match="exactly 3 components"):
            gprint("x", rgb=[255, 0])

    def test_too_many_components(self) -> None:
        with pytest.raises(InvalidRGBError, match="exactly 3 components"):
            gprint("x", rgb=[255, 0, 0, 0])

    def test_value_above_255(self) -> None:
        with pytest.raises(InvalidRGBError, match="must be 0-255"):
            gprint("x", rgb=[256, 0, 0])

    def test_negative_value(self) -> None:
        with pytest.raises(InvalidRGBError, match="must be 0-255"):
            gprint("x", rgb=[-1, 0, 0])

    def test_unrecognized_string(self) -> None:
        with pytest.raises(InvalidRGBError, match="Unrecognized color string"):
            gprint("x", rgb="invalid")

    def test_boolean_rejected(self) -> None:
        with pytest.raises(InvalidRGBError, match="must be an int"):
            gprint("x", rgb=[True, 0, 0])

    def test_float_rejected(self) -> None:
        with pytest.raises(InvalidRGBError, match="must be an int"):
            gprint("x", rgb=[255.0, 0, 0])  # type: ignore[list-item]

    def test_string_in_list_rejected(self) -> None:
        with pytest.raises(InvalidRGBError, match="must be an int"):
            gprint("x", rgb=["255", "0", "0"])  # type: ignore[list-item]

    def test_non_sequence_rejected(self) -> None:
        with pytest.raises(InvalidRGBError, match="list or tuple"):
            gprint("x", rgb=12345)  # type: ignore[arg-type]

    def test_exception_hierarchy(self) -> None:
        """InvalidRGBError should be catchable as ValueError and GprintError."""
        with pytest.raises(ValueError):
            gprint("x", rgb=[999, 0, 0])
        with pytest.raises(GprintError):
            gprint("x", rgb=[999, 0, 0])


# ── Color constants ──────────────────────────────────────────────────────────


class TestColorConstants:
    """Verify integrity of color constants."""

    def test_colors_are_tuples(self) -> None:
        """All predefined colors must be immutable tuples."""
        assert isinstance(RED, tuple)
        assert isinstance(BLUE, tuple)
        assert isinstance(WHITE, tuple)

    def test_colors_immutable(self) -> None:
        """Color constants should not be modifiable."""
        with pytest.raises(TypeError):
            RED[0] = 128  # type: ignore[index]
