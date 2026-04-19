#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "4" for an input of "2 + 2"
assert run("2 + 2").output == "4"

# Checks that the program outputs "9" for an input of "3 * 3"
assert run("3 * 3").output == "9"

###

print("All tests passed!")
