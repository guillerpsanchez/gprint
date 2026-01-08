"""Tests for gprint module."""
import pytest
from gprint import gprint, InvalidRGBError, RED, BLUE, get_random


class TestGprintBasic:
    """Basic functionality tests."""
    
    def test_default_color(self, capsys):
        """Test printing with default color."""
        gprint("Hello world")
        captured = capsys.readouterr()
        assert captured.out == "Hello world\n"
    
    def test_no_newline(self, capsys):
        """Test printing without newline."""
        gprint("Hello world", new_line=False)
        captured = capsys.readouterr()
        assert captured.out == "Hello world"
    
    def test_return_default(self):
        """Test returning message with default color."""
        result = gprint("Hello world", return_me=True)
        assert result == "Hello world"


class TestGprintColors:
    """Color-related tests."""
    
    def test_rgb_list(self, capsys):
        """Test printing with RGB list."""
        gprint("Red text", rgb=[255, 0, 0])
        captured = capsys.readouterr()
        assert captured.out == "\033[38;2;255;0;0mRed text\u001b[0m\n"
    
    def test_predefined_color_red(self, capsys):
        """Test printing with predefined RED color."""
        gprint("Red text", rgb=RED)
        captured = capsys.readouterr()
        assert captured.out == "\033[38;2;255;0;0mRed text\u001b[0m\n"
    
    def test_predefined_color_blue(self, capsys):
        """Test printing with predefined BLUE color."""
        gprint("Blue text", rgb=BLUE)
        captured = capsys.readouterr()
        assert captured.out == "\033[38;2;0;0;255mBlue text\u001b[0m\n"
    
    def test_return_colored(self):
        """Test returning colored string."""
        result = gprint("Red text", rgb=[255, 0, 0], return_me=True)
        assert result == "\033[38;2;255;0;0mRed text\u001b[0m"
    
    def test_random_color(self, capsys):
        """Test RANDOM color produces colored output."""
        gprint("Random", rgb="RANDOM")
        captured = capsys.readouterr()
        # Should have ANSI codes
        assert "\033[38;2;" in captured.out
        assert "\u001b[0m" in captured.out


class TestRainbowMode:
    """Rainbow mode tests."""
    
    def test_rainbow_mode(self, capsys):
        """Test rainbow mode prints each character in different color."""
        gprint("ABC", rainbow_mode=True)
        captured = capsys.readouterr()
        # Should have multiple ANSI codes (one per character)
        assert captured.out.count("\033[38;2;") == 3
    
    def test_rainbow_mode_return(self):
        """Test rainbow mode with return_me."""
        result = gprint("AB", rainbow_mode=True, return_me=True)
        # Should have ANSI codes for each character
        assert result.count("\033[38;2;") == 2


class TestGetRandom:
    """Tests for get_random function."""
    
    def test_returns_valid_rgb(self):
        """Test that get_random returns a valid RGB list."""
        color = get_random()
        assert isinstance(color, list)
        assert len(color) == 3
        assert all(isinstance(v, int) for v in color)
        assert all(0 <= v <= 255 for v in color)


class TestInvalidInput:
    """Tests for error handling."""
    
    def test_invalid_rgb_too_few_values(self):
        """Test that RGB with fewer than 3 values raises error."""
        with pytest.raises(InvalidRGBError, match="Invalid RGB code provided"):
            gprint("Test", rgb=[255, 0])
    
    def test_invalid_rgb_too_many_values(self):
        """Test that RGB with more than 3 values raises error."""
        with pytest.raises(InvalidRGBError, match="Invalid RGB code provided"):
            gprint("Test", rgb=[255, 0, 0, 0])
    
    def test_invalid_rgb_out_of_range(self):
        """Test that RGB values outside 0-255 raise error."""
        with pytest.raises(InvalidRGBError, match="Invalid RGB code provided"):
            gprint("Test", rgb=[256, 0, 0])
    
    def test_invalid_rgb_negative(self):
        """Test that negative RGB values raise error."""
        with pytest.raises(InvalidRGBError, match="Invalid RGB code provided"):
            gprint("Test", rgb=[-1, 0, 0])
    
    def test_invalid_rgb_string(self):
        """Test that invalid string raises error."""
        with pytest.raises(InvalidRGBError, match="Invalid RGB code provided"):
            gprint("Test", rgb="invalid")
