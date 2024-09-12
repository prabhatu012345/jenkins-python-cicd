# tests/test_hello.py
import io
import sys
from hello_world.hello import say_hello

def test_say_hello(capfd):
    say_hello()
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"
