#!../../.venv/bin/python
"""
Module to print P-Entropizer ASCII banner
"""

from colorama import Fore

def print_banner() -> None:
    """Print P-Entropizer ASCII banner"""

    print(Fore.LIGHTMAGENTA_EX)
    print("""
    ____        ______      __                   _                
   / __ \\      / ____/___  / /__________  ____  (_)___  ___  _____
  / /_/ /_____/ __/ / __ \\/ __/ ___/ __ \\/ __ \\/ /_  / / _ \\/ ___/
 / ____/_____/ /___/ / / / /_/ /  / /_/ / /_/ / / / /_/  __/ /
/_/         /_____/_/ /_/\\__/_/   \\____/ .___/_/ /___/\\___/_/
                                      /_/
""")
    print(Fore.RESET)
