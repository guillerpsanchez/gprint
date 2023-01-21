def test_basic():
    assert gprint("Hola mundo") == "Hola mundo"

def test_rgb_code():
    assert gprint("Hola mundo", rgb=[255,0,0]) == "\033[38;2;255;0;0mHola mundo\u001b[0m"

def test_rainbow_mode():
    assert gprint("Hola mundo", rainbow_mode=True) != "Hola mundo"

def test_no_newline():
    assert gprint("Hola mundo", new_line=False) == "Hola mundo"

def test_return_me():
    assert gprint("Hola mundo", return_me=True) == "Hola mundo"

def test_invalid_rgb():
    with pytest.raises(rgb_string_not_valid):
        gprint("Hola mundo", rgb=[255,0])