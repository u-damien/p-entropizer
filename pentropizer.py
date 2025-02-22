from colorama import Fore
import math
import humanfriendly
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="P-Entropizer. Calculate password entropy and the time to be cracked")
    
    # Argument optionnel pour le hash
    parser.add_argument("-r", "--hash-rate", type=int, help="Hashrate H/s capability of your hardware", required=False)
    
    # Argument positionnel pour le mot de passe
    parser.add_argument("password", type=str, help="Password to analyze", nargs='?', default=None)
    
    args = parser.parse_args()
    
    return args.password, args.hash_rate

def init_program() -> None:

    print(Fore.LIGHTMAGENTA_EX)
    print(f"""
    ____        ______      __                   _                
   / __ \\      / ____/___  / /__________  ____  (_)___  ___  _____
  / /_/ /_____/ __/ / __ \\/ __/ ___/ __ \\/ __ \\/ /_  / / _ \\/ ___/
 / ____/_____/ /___/ / / / /_/ /  / /_/ / /_/ / / / /_/  __/ /    
/_/         /_____/_/ /_/\\__/_/   \\____/ .___/_/ /___/\\___/_/     
                                      /_/                         
""")   
    print(Fore.RESET)
    password, hash_rate = parse_arguments()
    print(f"{Fore.LIGHTBLACK_EX}Press Ctrl+C to exit.\n")
    print(f"Recommanded entropy is > 75.")
    print("Strong password is 20 characters including lower/upper case letter, number and specials characters.\n")
    print("P-Entropizer do not consider wordlists of password available to calculate the robustness of a password.")
    print("It calculates according pure brute force methods.\n")

    return password, hash_rate
    
def raise_error(error_msg: str):
    print(f"{Fore.RED}[!]{Fore.LIGHTRED_EX} ERROR: {error_msg}{Fore.RESET}")
    exit(1)

def ask_password() -> str:
    verified = False
    while not verified:
        pass_input = input(f"{Fore.BLUE}[#]{Fore.LIGHTBLUE_EX} Please enter your password: {Fore.RESET}")
        if len(pass_input) > 0:
            verified = True
        else:
            print(f"{Fore.RED}[-] Password must be at least 1 character!{Fore.RESET}")
    return pass_input

def get_formula_parameters(password: str) -> list[int, int]:
    """_summary_
    formula: E=L⋅log₂(R)
    Args:
        password (str): _description_
    """
    def get_chars_range(password: str) -> int:
        """
        Get range of possible utf8 printable characters of the password.
        Calculate range by calculating distance between lower and higher unicode code point
        """
        def print_complexity(name: str, contains: bool):
            print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Contains {Fore.CYAN}{name}{Fore.LIGHTBLUE_EX}: {Fore.GREEN if contains else Fore.RED}{contains}{Fore.RESET}")

        contains_digits = any([char.isdigit() for char in list(password)])
        print_complexity("digits [0-9]", contains_digits)

        contains_lower = any([char.islower() for char in list(password)])
        print_complexity("lower [a-z]", contains_lower)

        contains_upper = any([char.isupper() for char in list(password)])
        print_complexity("upper [A-Z]", contains_upper)

        contains_specials = any([(
            not char.isdigit() and 
            not char.islower() and 
            not char.isupper()
            ) for char in list(password)])
        print_complexity("specials [others]", contains_specials)
        print()

        sorted_unicode_array = sorted([ord(char) for char in list(password)])
        min, max = sorted_unicode_array[0], sorted_unicode_array[-1]
        chars_range = max-min + 1
        return chars_range
    
    def get_password_length(password: str) -> int:
        return len(password)
    
    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Password: {Fore.MAGENTA}{password}")
    R = get_chars_range(password)
    L = get_password_length(password)
    return R, L


def calculate_entropy(R: int, L: int) -> int:
    if not isinstance(R, int) or not isinstance(L, int):
        raise_error(f"One or more parameter are not integers.\nR: {R} -> {type(R)}\nL: {L} -> {type(L)}")
    
    E = L * math.log2(R)
    return E

def print_password_robustness(entropy: float):
    """
    Prints the password robustness information based on its entropy.

    Parameters:
        entropy (float): The entropy of the password in bits.
    """
    if entropy < 28:
        level = "Unacceptable"
        color = Fore.RED
        usage = "Not recommended for any secure authentication or data protection."
    elif entropy < 35:
        level = "Very Weak"
        color = Fore.LIGHTRED_EX
        usage = "Suitable only for non-critical, disposable accounts."
    elif entropy < 45:
        level = "Weak"
        color = Fore.YELLOW
        usage = "May be acceptable for temporary accounts with minimal risk."
    elif entropy < 60:
        level = "Moderate"
        color = Fore.LIGHTYELLOW_EX
        usage = "Appropriate for low-risk environments; not for sensitive information."
    elif entropy < 80:
        level = "Adequate"
        color = Fore.CYAN
        usage = "Suitable for standard online services with moderate security requirements."
    elif entropy < 100:
        level = "Strong"
        color = Fore.GREEN
        usage = "Recommended for general-purpose accounts, such as email and social media."
    elif entropy < 120:
        level = "Very Strong"
        color = Fore.LIGHTGREEN_EX
        usage = "Appropriate for online banking and protecting critical personal data."
    elif entropy < 140:
        level = "Highly Secure"
        color = Fore.BLUE
        usage = "Suitable for protecting sensitive business or proprietary information."
    elif entropy < 160:
        level = "Extremely Secure"
        color = Fore.MAGENTA
        usage = "Recommended for high-security environments and enterprise-level systems."
    else:  # entropy >= 161
        level = "Maximum Security"
        color = Fore.LIGHTMAGENTA_EX
        usage = "Reserved for mission-critical systems and top-secret data where maximum protection is essential."

    # Print the results with the designated color
    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Your password entropy is equal to: {color}{entropy}")
    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Strength Level: {color}{level}")
    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Secure Usage: {color}{usage}")
    print(Fore.RESET)

def calculate_time_to_crack(entropy: float, hash_rate: int=None):
    """Calculate time in seconds to crack the password
    Formula:
    T_average = (2^E) / (2*h)

    Args:
        entropy (float): password entropy
        h (int): hash per second
    """
    UNIVERSE_AGE_SECONDS = 4.35252e+17
    def print_result(result):
        try:
            human_result = humanfriendly.format_timespan(result, detailed=True)
            times_universe = f"{round(result/UNIVERSE_AGE_SECONDS, 6)} times the age of the universe."
        except humanfriendly.decimal.InvalidOperation:
            human_result = f"{Fore.GREEN}Eternity!"
            times_universe = "Too much universes!"
        print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Scientific notation: {Fore.MAGENTA}{result}.")
        print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Human readable: {Fore.MAGENTA}{human_result if human_result else "Instantly"}.")
        print(f"{Fore.BLUE}[~]{Fore.MAGENTA} {times_universe}")

    if hash_rate is None:
        # Cracking time example with different hardwares
        # SHA2-256 time average
        RYZEN55600G_HRATE = 41.49e+6 #  41.49 MH/s for entry-level CPU
        RTX5090_HRATE = 28.35e+9   # ~28.35 GH/s   for high-end GPU
        
        # Result in seconds
        entry_level_time = (2**entropy) / (2*RYZEN55600G_HRATE)
        high_end_time = (2**entropy) / (2*RTX5090_HRATE)

        print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Cracking time for {Fore.MAGENTA}SHA2-256{Fore.LIGHTBLUE_EX} hash of your password\n")

        print(f"{Fore.BLUE}[~] Ryzen 5 5600G{Fore.LIGHTBLUE_EX} (Entry-Level CPU ~41.49 MH/s):")
        print_result(entry_level_time)
        
        print()

        print(f"{Fore.BLUE}[~] NVIDIA Geforce RTX 5090{Fore.LIGHTBLUE_EX} (High-End GPU ~28.35 GH/s):")
        print_result(high_end_time)

    else:
        # Cracking time according provided hashrate
        cracking_time = (2**entropy) / (2*hash_rate)

        print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Cracking time for of your password with {Fore.MAGENTA}{humanfriendly.format_size(hash_rate, binary=False).replace("bytes", "").replace("B", "")}H/s{Fore.LIGHTBLUE_EX} rate:")
        print_result(cracking_time)

    

def main() -> None:
    password, hash_rate = init_program()

    if password is None:
        password = ask_password()
    
    R, L = get_formula_parameters(password)
    password_entropy = calculate_entropy(R, L)
    print_password_robustness(password_entropy)
    calculate_time_to_crack(password_entropy, hash_rate)
    print(f"\n{Fore.GREEN}[+]{Fore.LIGHTGREEN_EX} Done!{Fore.RESET}")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTRED_EX} Exited{Fore.RESET}")
