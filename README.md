# Password Strength Checker

**Password Strength Checker** is a Python library designed to help developers evaluate the strength of passwords and verify their presence in the RockYou leaked password dataset. The library provides flexibility with customizable criteria and can be easily integrated into Python projects.

---

## Features

- **Password Strength Evaluation**:
  - Customizable criteria, including:
    - Minimum password length
    - Number of uppercase and lowercase letters
    - Number of digits and special characters
  - Provides a detailed strength rating: *Very Weak*, *Weak*, *Medium*, *Strong*, and *Very Strong*.
- **Leaked Password Detection**:
  - Checks passwords against the RockYou dataset to identify potential vulnerabilities.
- **Ease of Integration**:
  - Lightweight and modular design for seamless integration into existing Python projects.

---

## Installation

Install the library from PyPI:

## Usage 

```bash
from password_strength_checker import PasswordStrengthChecker

# Create an instance with your criteria
checker = PasswordStrengthChecker(
    password="MyStrongP@ssw0rd!",
    min_length=8,
    min_uppercase=1,
    min_lowercase=1,
    min_digits=1,
    min_special_chars=1
)

# Evaluate the password
result = checker.is_valid()
print(result)
```


```bash
pip install password-strength-checker-pro
