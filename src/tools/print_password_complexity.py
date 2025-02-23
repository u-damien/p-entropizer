#!../../.venv/bin/python
"""
Module to print P-Entropizer password complexity
"""

from colorama import Fore

def __print_complexity(name: str, contains: bool):
    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Contains {Fore.CYAN}" +
        f"{name}{Fore.LIGHTBLUE_EX}: " +
        f"{Fore.GREEN if contains else Fore.RED}{contains}{Fore.RESET}"
    )

def print_password_complexity(password: str):
    """Print password complexity"""
    contains_digits = any(char.isdigit() for char in list(password))
    __print_complexity("digits [0-9]", contains_digits)

    contains_lower = any(char.islower() for char in list(password))
    __print_complexity("lower [a-z]", contains_lower)

    contains_upper = any(char.isupper() for char in list(password))
    __print_complexity("upper [A-Z]", contains_upper)

    contains_specials = any((
        not char.isdigit() and
        not char.islower() and
        not char.isupper()
        ) for char in list(password))
    __print_complexity("specials [others]", contains_specials)
    print()
