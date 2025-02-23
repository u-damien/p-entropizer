#!venv/bin/python
"""
Filename    : pentropizer.py
Porject     : P-Entropizer
Description : Main module for P-Entropizer, this tool provide an analyzer for
            password entropy and estimate the time required to crack it using
            brute-force methods
"""

import sys
import argparse
from colorama import Fore

from src.tools.print_password_robustness import print_password_robustness
from src.calculate_password_entropy import calculate_entropy
from src.calc_time_to_crack import calculate_time_to_crack
from src.tools.print_description import print_description
from src.tools.print_banner import print_banner

def parse_arguments():
    """Parse CLI arguments"""
    parser = argparse.ArgumentParser(description="P-Entropizer. Calculate " +
        "password entropy and the time to be cracked"
    )
    parser.add_argument("-r", "--hash-rate", type=int, required=False,
        help="Hashrate H/s capability of your hardware"
    )
    parser.add_argument("password", type=str, help="Password to analyze",
        nargs='?', default=None
    )
    args = parser.parse_args()

    return args.password, args.hash_rate

def ask_password() -> str:
    """Ask user to input a password"""
    verified = False
    while not verified:
        pass_input = input(f"{Fore.BLUE}[#]{Fore.LIGHTBLUE_EX} Please enter " +
            f"your password: {Fore.RESET}"
        )
        if len(pass_input) > 0:
            verified = True
        else:
            print(f"{Fore.RED}[-] Password must be at least 1 " +
                f"character!{Fore.RESET}"
            )
    return pass_input

def main() -> None:
    """Main function to run the program
    
    To run it require read specifics CLI command args.
    """
    print_banner()
    password, hash_rate = parse_arguments()
    print_description()

    if password is None:
        password = ask_password()
    password_entropy = calculate_entropy(password)
    print_password_robustness(password_entropy)
    calculate_time_to_crack(password_entropy, hash_rate)
    print(f"\n{Fore.GREEN}[+]{Fore.LIGHTGREEN_EX} Done!{Fore.RESET}")
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTRED_EX} Exited{Fore.RESET}")
