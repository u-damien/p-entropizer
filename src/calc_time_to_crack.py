#!#!../.venv/bin/python
"""
Module to calculate time to crack the password
"""

import humanfriendly
from colorama import Fore

# Cracking time example with different hardwares, SHA2-256 time average
RYZEN55600G_HRATE = 41.49e+6    #  41.49 MH/s for entry-level CPU
RTX5090_HRATE = 28.35e+9        # ~28.35 GH/s   for high-end GPU
UNIVERSE_AGE_SECONDS = 4.35252e+17

def __print_result(result) -> None:
    """Print result"""
    try:
        human_result = humanfriendly.format_timespan(result, detailed=True)
        times_universe = (f"{round(result/UNIVERSE_AGE_SECONDS, 6)} " +
            "times the age of the universe."
        )
    except humanfriendly.decimal.InvalidOperation:
        human_result = f"{Fore.GREEN}Eternity!"
        times_universe = "Too much universes!"
    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Scientific notation: " +
        f"{Fore.MAGENTA}{result}.\n{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} " +
        f"Human readable: {Fore.MAGENTA}" +
        f"{human_result if human_result else 'Instantly'}." +
        f"{Fore.BLUE}[~]{Fore.MAGENTA} {times_universe}"
    )

def __calculate_for_default_consumer_grade_hardware(entropy: float) -> None:
    """Calculate time to crack the password using default consumer grade 
    hardware"""
    # Result in seconds
    entry_level_time = (2**entropy) / (2*RYZEN55600G_HRATE)
    high_end_time = (2**entropy) / (2*RTX5090_HRATE)

    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Cracking time for " +
        f"{Fore.MAGENTA}SHA2-256{Fore.LIGHTBLUE_EX} hash of your " +
        f"password\n{Fore.BLUE}[~] Ryzen 5 5600G{Fore.LIGHTBLUE_EX} " +
        "(Entry-Level CPU ~41.49 MH/s):"
    )
    __print_result(entry_level_time)
    print(f"\n{Fore.BLUE}[~] NVIDIA Geforce RTX 5090{Fore.LIGHTBLUE_EX} " +
        "(High-End GPU ~28.35 GH/s):"
    )
    __print_result(high_end_time)

def __calculate_for_custom_hash_rate(entropy: float, hash_rate: int):
    """Calculate time to crack the password using a custom hash rate"""
    # Cracking time according provided hashrate
    cracking_time = (2**entropy) / (2*hash_rate)
    readable_hash_rate = (humanfriendly
        .format_size(hash_rate, binary=False)
        .replace("bytes", '')
        .replace('B', '')
    )

    print(f"{Fore.BLUE}[~]{Fore.LIGHTBLUE_EX} Cracking time for of your " +
        f"password with {Fore.MAGENTA}" +
        f"{readable_hash_rate}H/s{Fore.LIGHTBLUE_EX} rate:")
    __print_result(cracking_time)

def calculate_time_to_crack(entropy: float, hash_rate: int=None):
    """Calculate time in seconds to crack the password
    Formula:
    T_average = (2^E) / (2*h)

    Args:
        entropy (float): password entropy
        h (int): hash per second
    """
    if hash_rate is None:
        __calculate_for_default_consumer_grade_hardware(entropy)
    else:
        __calculate_for_custom_hash_rate(entropy, hash_rate)
