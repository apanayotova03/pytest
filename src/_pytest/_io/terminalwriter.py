"""Helper functions for writing to terminals and files."""

import os
import shutil
import sys
from typing import final, Literal, Optional, Sequence, TextIO, TYPE_CHECKING

if TYPE_CHECKING:
    from pygments.formatter import Formatter
    from pygments.lexer import Lexer

def get_terminal_width() -> int:
    width, _ = shutil.get_terminal_size(fallback=(80, 24))
    if width < 40:
        width = 80
    return width

def should_do_markup(file: TextIO) -> bool:
    if os.environ.get("PY_COLORS") == "1":
        return True
    if os.environ.get("PY_COLORS") == "0":
        return False
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    return (
        hasattr(file, "isatty") and file.isatty() and os.environ.get("TERM") != "dumb"
    )

@final
class TerminalWriter:
    _esctable = dict(
        black=30, red=31, green=32, yellow=33, blue=34, purple=35, cyan=36, white=37,
        Black=40, Red=41, Green=42, Yellow=43, Blue=44, Purple=45, Cyan=46, White=47,
        bold=1, light=2, blink=5, invert=7
    )
    
    def __init__(self, file: Optional[TextIO] = None):
        if file is None:
            file = sys.stdout
        if hasattr(file, "isatty") and file.isatty() and sys.platform == "win32":
            try:
                import colorama
                file = colorama.AnsiToWin32(file).stream
            except ImportError:
                pass
        self._file = file
        self.hasmarkup = should_do_markup(file)
        self._current_line = ""
        self._terminal_width = None
        self.code_highlight = True
        self.branch_tracker = [0, 0]  # For fullwidth
        self.markup_branch_tracker = [0, 0, 0, 0, 0, 0]  # Initialize markup branch tracking

    @property
    def fullwidth(self) -> int:
        if self._terminal_width is not None:
            self.branch_tracker[0] = 1  # Mark branch 1 as taken
            return self._terminal_width
        else:
            self.branch_tracker[1] = 1  # Mark branch 2 as taken
            return get_terminal_width()

    @fullwidth.setter
    def fullwidth(self, value: int):
        self._terminal_width = value

    def report_branch_usage(self):
        return self.branch_tracker  # Return the branch usage array

    def markup(self, text: str, **markup: bool) -> str:
        for name in markup:
            if name not in self._esctable:
                self.markup_branch_tracker[0] = 1  # Mark branch 1 as taken
                return f"Error: unknown markup: {name!r}"
            else:
                self.markup_branch_tracker[1] = 1  # Mark branch 2 as taken

        if self.hasmarkup:
            self.markup_branch_tracker[2] = 1  # Mark branch 3 as taken
            esc = [self._esctable[name] for name, on in markup.items() if on]
            if esc:
                self.markup_branch_tracker[3] = 1  # Mark branch 4 as taken
                text = "".join(f"\x1b[{cod}m" for cod in esc) + text + "\x1b[0m"
            else:
                self.markup_branch_tracker[4] = 1  # Mark branch 5 as taken
        else:
            self.markup_branch_tracker[5] = 1  # Mark branch 6 as taken
        return text

    def report_markup_branch_usage(self):
        return self.markup_branch_tracker

def main():
    tw = TerminalWriter()
    
    # Test the fullwidth function
    print("Testing fullwidth with _terminal_width set to None:")
    tw.fullwidth  # Accessing fullwidth to trigger the property
    branch_one, branch_two = tw.report_branch_usage()
    print(f"Branch one was: {branch_one}\nBranch two was: {branch_two}\n")
    
    tw.branch_tracker = [0, 0]
    print("Testing fullwidth with _terminal_width set to 100:")
    tw.fullwidth = 100  # Setting a specific width
    tw.fullwidth  # Accessing fullwidth again to use the setter value
    branch_one, branch_two = tw.report_branch_usage()
    print(f"Branch one was: {branch_one}\nBranch two was: {branch_two}\n")

    # Test the markup function
    tw.markup_branch_tracker = [0, 0, 0, 0, 0, 0]
    print("Testing markup with known markup key and esc list non-empty:")
    tw.markup("Test", bold=True)
    print("Branches taken:", tw.report_markup_branch_usage())

    tw.markup_branch_tracker = [0, 0, 0, 0, 0, 0]
    print("Testing markup with known markup key and esc list empty:")
    tw.markup("Test", bold=False)
    print("Branches taken:", tw.report_markup_branch_usage())

    tw.markup_branch_tracker = [0, 0, 0, 0, 0, 0]
    print("Testing markup with unknown markup key:")
    tw.markup("Test", wrongkey=True)
    print("Branches taken:", tw.report_markup_branch_usage())

    tw.hasmarkup = False
    tw.markup_branch_tracker = [0, 0, 0, 0, 0, 0]
    print("Testing markup with hasmarkup set to False:")
    tw.markup("Test", bold=True)
    print("Branches taken:", tw.report_markup_branch_usage())

if __name__ == "__main__":
    main()
