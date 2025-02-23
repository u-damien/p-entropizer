<h1 align="center"> P-Entropizer</h1>

<p align="center">P-Entropizer is a Python-based tool for analyzing password entropy and estimating the time required to crack it using brute-force methods. It provides a detailed evaluation of password strength based on character complexity and entropy calculations.</p>

## Mathematical Formulae

### Password Entropy

$E = L \cdot \log_2(R)$

$E$: Password entropy.<br>
$L$: Password length.<br>
$R$: Range of characters.

### Cracking duration

$T_{\text{average}} = \frac{2^E}{2 \cdot h}$

$T_{\text{average}}$: Average duration of cracking in seconds. <br>
$E$: Password entropy previously calculated.<br>
$h$: Hashrate in H/s.

## Features
- Calculates password entropy based on character set and length.
- Two example of cracking duration if no hashrate provided (Ryzen 5 5600G & RTX 5090).
- Provides a security level rating for the analyzed password.
- Supports both interactive input and command-line arguments.

## Installation
Ensure you have `git` and `python3` installed.

```bash
git clone https://github.com/u-damien/p-entropizer.git
cd p-entropizer
pip install -r requirements.txt
python3 pentropizer.py -h
```

## Usage
### Command-Line Execution
You can run the script directly with a password argument and an optional hash rate:

```bash
python3 pentropizer.py "your_password" -r 5000000
```

- `your_password`:  The password you want to analyze.
- `-r, --hash-rate`: (Optional) Hashing speed in hashes per second (H/s).

### Interactive Mode
If no password is provided as an argument, the script will prompt you to enter one interactively.

```bash
python3 pentropizer.py
```

## Example Output
![image](https://github.com/user-attachments/assets/acbc0e4d-f497-4cb1-bd0b-05b764db5115)

## Notes
- This tool does **not** consider password dictionaries or known weak passwords.
- The time-to-crack estimate assumes pure brute-force attacks without optimizations.

## Development

To develop this project we use a venv for testing with a dedicated 
requirements.txt called dev.txt, it embed lynting and security tool.

### Testing linting (Quality)

We use pylint, you could use it like that :
```sh
pylint pentropizer.py src/*.py src/tools/*.py
```

As pylint will check import, make sure the file `.pylintrc` is well configured.

### Security testing

We use bandit, you could use it like that :
```sh
bandit . -r --exclude "./.dev,./.venv"
```

## License
This project is licensed under the MIT License.
