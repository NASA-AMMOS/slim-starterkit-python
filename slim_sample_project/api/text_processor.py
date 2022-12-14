# Sample code: REPLACE with project code.
from colorama import Fore, Back, Style
from random import randint


class TextWriter:
    """
    Generic class to write pre-formatted text to terminal.

    Class attribute `color` tracks a provided, or alternately randomly set text color.
    """
    def __init__(self, color=None):
        """
        Initialization method for TextWriter class.
        :param color:
        :type color: AnsiFore
        @param color:  A Colorama ANSI color Enum value used
            to display provided text characters.
        @type color: Fore
        """
        if not color:
            self.color = [Fore.CYAN, Fore.BLACK, Fore.YELLOW][randint(0, 2)]
        else:
            self.color = str(color) if str(color) in vars(Fore) else Fore.YELLOW
        self.bg = [Back.LIGHTBLUE_EX, Back.LIGHTWHITE_EX, Back.LIGHTRED_EX][randint(0, 2)]
        self.style = [Style.BRIGHT, Style.NORMAL][randint(0, 1)]

    def out(self, text):
        """
        Output writer to apply color settings to terminal text.
        :param text: The value to write to a string.
        :type text: Any type that supports an internal str reporesentation.
        """
        if not text:
            text = "Hello World"
        print(self.color, self.bg, self.style, str(text), Style.RESET_ALL)
