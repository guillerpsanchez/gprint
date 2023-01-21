from gprint import *
import pytest

def test_basic(capsys):
    gprint("Hola mundo")
    captured = capsys.readouterr()
    assert captured.out == "Hola mundo\n"

def test_rgb_code(capsys):
    gprint("Hola mundo", rgb=[255,0,0])
    captured = capsys.readouterr()
    assert captured.out == "\033[38;2;255;0;0mHola mundo\u001b[0m\n"

def test_rainbow_mode(capsys):
    gprint("Hola mundo", rainbow_mode=True)
    captured = capsys.readouterr()
    assert captured.out != "Hola mundo\n"

def test_no_newline(capsys):
    gprint("Hola mundo", new_line=False)
    captured = capsys.readouterr()
    assert captured.out == "Hola mundo"

def test_return_me():
    assert gprint("Hola mundo", return_me=True) == "Hola mundo"

def test_invalid_rgb(capsys):
    try:
        gprint("Hola mundo", rgb=[255,0])
    except InvalidRGBError as e:
        assert str(e) == "Invalid RGB code provided"