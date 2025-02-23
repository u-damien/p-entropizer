#!#!../.venv/bin/python
"""
Module to calculate password entropy
"""

import sys
import math
from colorama import Fore

from src.tools.print_password_complexity import print_password_complexity

def __raise_error(error_msg: str):
    """Raise error"""
    print(f"{Fore.RED}[!]{Fore.LIGHTRED_EX} ERROR: {error_msg}{Fore.RESET}")
    sys.exit(1)

def __get_chars_range(password: str) -> int:
    """
    Get range of possible utf8 printable characters of the password.
    Calculate range by calculating distance between lower and higher unicode 
    code point
    """
    sorted_unicode_array = sorted([ord(char) for char in list(password)])
    min_unicode = sorted_unicode_array[0]
    max_unicode = sorted_unicode_array[-1]
    chars_range = max_unicode - min_unicode + 1

    return chars_range

def __get_formula_parameters(password: str) -> list[int, int]:
    """_summary_
    formula:            E=L⋅log₂(R)
    or:     password_entropy = password_length * log₂(range_of_characters)
    Args:
        password (str): _description_
    """
    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Password: {Fore.MAGENTA}{password}")
    print_password_complexity(password)
    range_of_characters = __get_chars_range(password)
    password_length = len(password)
    return range_of_characters, password_length

def calculate_entropy(password: str) -> int:
    """Calculate the password entropy"""
    range_of_characters, password_length = __get_formula_parameters(password)
    if (not isinstance(range_of_characters, int) or
        not isinstance(password_length, int)):
        __raise_error("One or more parameter are not integers.\nR: " +
            f"{range_of_characters} -> {type(range_of_characters)}\nL: " +
            f"{password_length} -> {type(password_length)}"
        )

    password_entropy = password_length * math.log2(range_of_characters)
    return password_entropy
