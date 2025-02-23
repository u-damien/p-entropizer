#!../../.venv/bin/python
"""
Module to print P-Entropizer description
"""

from colorama import Fore

def print_description() -> None:
    """Print P-Entropizer description"""

    print(f"{Fore.LIGHTBLACK_EX}Press Ctrl+C to exit.\n")
    print("Recommanded entropy is > 75.\nStrong password is 20 characters " +
        "including lower/upper case letter, number and specials characters.\n" +
        "P-Entropizer do not consider wordlists of password available to " +
        "calculate the robustness of a password.\nIt calculates according " +
        "pure brute force methods.\n"
    )
