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
## Explanation

- **Password:** The password string you want to check.
- **min_length:** The minimum length your password should have.
- **min_uppercase:**  The minimum number of uppercase letters.
- **min_lowercase:**  The minimum number of lowercase letters.
- **min_digits:** The minimum number of digits.
- **min_special_chars:**  The minimum number of special characters required.
- **The is_valid()**  method will return:The strength of the password (e.g., "Very Strong", "Weak").
Whether the password has been found in the RockYou leaked password dataset.

```bash
pip install password-strength-checker-pro
