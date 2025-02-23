#!../../.venv/bin/python
"""
Module to print P-Entropizer password robustness
"""

import json
from colorama import Fore

COLOR_DICTIONARY = {
    "RED": Fore.RED,
    "LIGHTRED_EX": Fore.LIGHTRED_EX,
    "YELLOW": Fore.YELLOW,
    "LIGHTYELLOW_EX": Fore.LIGHTYELLOW_EX,
    "CYAN": Fore.CYAN,
    "GREEN": Fore.GREEN,
    "LIGHTGREEN_EX": Fore.LIGHTGREEN_EX,
    "BLUE": Fore.BLUE,
    "MAGENTA": Fore.MAGENTA
}

def __get_entropy_category(entropy: float):
    """Get the entropy level of the password."""
    with open("entropy_levels.json", encoding = "UTF8") as file:
        entropy_levels = json.load(file)
    for entry in entropy_levels:
        if entropy < entry["threshold"]:
            return (COLOR_DICTIONARY.get(entry["color"], Fore.WHITE),
                entry["level"], entry["usage"]
            )
    return ("Maximum Security", Fore.MAGENTA, "Reserved for mission-critical " +
        "systems and top-secret data where maximum protection is essential."
    )


def print_password_robustness(entropy: float):
    """
    Prints the password robustness information based on its entropy.

    Parameters:
        entropy (float): The entropy of the password in bits.
    """
    color, level, usage = __get_entropy_category(entropy)

    # Print the results with the designated color
    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Your password entropy is " +
        f"equal to: {color}{entropy}\n{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} " +
        f"Strength Level: {color}{level}\n{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} " +
        f"Secure Usage: {color}{usage}{Fore.RESET}\n")
