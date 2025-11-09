from gprint import *
import pytest


def test_basic(capsys):
    """Test basic printing without color"""
    gprint("Hola mundo")
    captured = capsys.readouterr()
    assert captured.out == "Hola mundo\n"


def test_rgb_code(capsys):
    """Test printing with RGB color code"""
    gprint("Hola mundo", rgb=[255, 0, 0])
    captured = capsys.readouterr()
    assert captured.out == "\033[38;2;255;0;0mHola mundo\u001b[0m\n"


def test_rainbow_mode(capsys):
    """Test rainbow mode produces different output"""
    gprint("Hola mundo", rainbow_mode=True)
    captured = capsys.readouterr()
    assert captured.out != "Hola mundo\n"
    assert len(captured.out) > len("Hola mundo\n")


def test_no_newline(capsys):
    """Test printing without newline"""
    gprint("Hola mundo", new_line=False)
    captured = capsys.readouterr()
    assert captured.out == "Hola mundo"


def test_return_me():
    """Test returning colored string instead of printing"""
    assert gprint("Hola mundo", return_me=True) == "Hola mundo"


def test_invalid_rgb():
    """Test that invalid RGB raises exception"""
    with pytest.raises(InvalidRGBError) as excinfo:
        gprint("Hola mundo", rgb=[255, 0])
    assert str(excinfo.value) == "Invalid RGB code provided"


def test_rgb_code_with_return(capsys):
    """Test return_me with RGB color"""
    result = gprint("Test", rgb=[0, 255, 0], return_me=True)
    assert result == "\033[38;2;0;255;0mTest\u001b[0m"
    captured = capsys.readouterr()
    assert captured.out == ""


def test_rgb_code_no_newline(capsys):
    """Test RGB color without newline"""
    gprint("Test", rgb=[0, 0, 255], new_line=False)
    captured = capsys.readouterr()
    assert captured.out == "\033[38;2;0;0;255mTest\u001b[0m"


def test_color_constants(capsys):
    """Test using color constants"""
    gprint("Red text", rgb=RED)
    captured = capsys.readouterr()
    assert "\033[38;2;255;0;0m" in captured.out


def test_random_color(capsys):
    """Test RANDOM color option"""
    gprint("Random", rgb="RANDOM")
    captured = capsys.readouterr()
    assert "\033[38;2;" in captured.out
    assert captured.out != "Random\n"


def test_get_random_returns_valid_color():
    """Test that get_random() returns a valid RGB list"""
    color = get_random()
    assert isinstance(color, list)
    assert len(color) == 3
    assert all(0 <= int(x) <= 255 for x in color)


def test_rainbow_mode_with_return():
    """Test rainbow mode with return_me option"""
    result = gprint("ABC", rainbow_mode=True, return_me=True)
    assert "\033[38;2;" in result
    assert "ABC" in result or "A" in result


def test_invalid_rgb_out_of_range():
    """Test RGB values out of range"""
    with pytest.raises(InvalidRGBError):
        gprint("Test", rgb=[256, 0, 0])


def test_invalid_rgb_negative():
    """Test negative RGB values"""
    with pytest.raises(InvalidRGBError):
        gprint("Test", rgb=[-1, 0, 0])


def test_invalid_rgb_too_long():
    """Test RGB with more than 3 values"""
    with pytest.raises(InvalidRGBError):
        gprint("Test", rgb=[255, 0, 0, 100])


def test_default_color_explicit(capsys):
    """Test explicit 'default' color argument"""
    gprint("Test", rgb="default")
    captured = capsys.readouterr()
    assert captured.out == "Test\n"


def test_default_with_return():
    """Test default color with return_me"""
    result = gprint("Test", rgb="default", return_me=True)
    assert result == "Test"


def test_default_no_newline(capsys):
    """Test default color without newline"""
    gprint("Test", rgb="default", new_line=False)
    captured = capsys.readouterr()
    assert captured.out == "Test"


def test_empty_string(capsys):
    """Test printing empty string"""
    gprint("")
    captured = capsys.readouterr()
    assert captured.out == "\n"


def test_special_characters(capsys):
    """Test printing special characters"""
    gprint("Hello\tWorld\n!")
    captured = capsys.readouterr()
    assert "Hello\tWorld\n!" in captured.out


def test_unicode_characters(capsys):
    """Test printing unicode characters"""
    gprint("Hello 世界 🌍", rgb=[100, 150, 200])
    captured = capsys.readouterr()
    assert "世界" in captured.out
    assert "🌍" in captured.out


def test_boundary_rgb_values(capsys):
    """Test boundary RGB values (0,0,0) and (255,255,255)"""
    gprint("Black", rgb=[0, 0, 0])
    captured = capsys.readouterr()
    assert "\033[38;2;0;0;0m" in captured.out

    gprint("White", rgb=[255, 255, 255])
    captured = capsys.readouterr()
    assert "\033[38;2;255;255;255m" in captured.out