import os
import shutil
import sys
from typing import final, Literal, Optional, Sequence, TextIO, TYPE_CHECKING


from _pytest._io.terminalwriter import should_do_markup


if TYPE_CHECKING:
    from pygments.formatter import Formatter
    from pygments.lexer import Lexer


def test():
    # Branch Id 1
    os.environ["PY_COLORS"] = "1"
    test = should_do_markup(None)
    del os.environ["PY_COLORS"]
    assert test == True


    os.environ["PY_COLORS"] = "0"
    test = should_do_markup(None)
    del os.environ["PY_COLORS"]
    assert test == False


    # Branch Id 3
    os.environ["NO_COLOR"] = "1"
    test = should_do_markup(None)
    del os.environ["NO_COLOR"]
    assert test == False


    # Branch Id 4
    os.environ["FORCE_COLOR"] = "1"
    test = should_do_markup(None)
    del os.environ["FORCE_COLOR"]
    assert test == True


    # Branch Id 5
    test = should_do_markup(None)
    assert test == False


    # Ensure environment is reset
    os.environ["PY_COLORS"] = "1"


# Running the test function to verify its behavior
if _name_ == "_main_":
    test()
