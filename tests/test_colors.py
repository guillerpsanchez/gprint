"""Tests for the gprint._colors module."""

from __future__ import annotations

from gprint import ALL_COLORS, CHART_REUSE, CHARTREUSE, COLOR_NAMES, RGBColor


class TestColorPalette:
    """Tests for the colour palette metadata."""

    def test_all_colors_is_tuple(self) -> None:
        assert isinstance(ALL_COLORS, tuple)

    def test_all_colors_non_empty(self) -> None:
        assert len(ALL_COLORS) > 0

    def test_all_entries_are_valid_rgb(self) -> None:
        for color in ALL_COLORS:
            assert isinstance(color, tuple), f"{color!r} is not a tuple"
            assert len(color) == 3, f"{color!r} does not have 3 components"
            for v in color:
                assert isinstance(v, int) and 0 <= v <= 255, (
                    f"Invalid component {v!r} in {color!r}"
                )

    def test_color_names_dict_matches(self) -> None:
        """COLOR_NAMES must only contain valid 3-int tuples."""
        for name, color in COLOR_NAMES.items():
            assert isinstance(name, str)
            assert isinstance(color, tuple) and len(color) == 3

    def test_chart_reuse_alias(self) -> None:
        """CHART_REUSE must equal CHARTREUSE for backward compatibility."""
        assert CHART_REUSE == CHARTREUSE
