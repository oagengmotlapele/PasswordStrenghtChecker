import gzip
import os
from dataclasses import dataclass


@dataclass
class PasswordStrengthChecker:
    """
    A class to check the strength of a password based on several criteria, and to check
    if the password appears in the RockYou dataset, which contains leaked passwords.

    Attributes:
    password (str): The password to be checked.
    min_length (int): The minimum length required for the password. Default is 8.
    min_uppercase (int): The minimum number of uppercase characters required. Default is 1.
    min_lowercase (int): The minimum number of lowercase characters required. Default is 1.
    min_digits (int): The minimum number of digits required. Default is 1.
    min_special_chars (int): The minimum number of special characters required. Default is 1.
    rockyou_gz_file (str): The filename of the RockYou password dataset (default is 'rockyou.txt.gz').

    Methods:
    load_rockyou_dataset: Loads the RockYou dataset from a compressed .gz file.
    is_valid: Checks whether the password meets the strength criteria and if it is found in the RockYou dataset.
    calculate_password_strength: Calculates the strength of the password based on predefined criteria.
    password_in_leaked_dataset: Checks if the password is present in the RockYou dataset.
    """

    password: str
    min_length: int = 8
    min_uppercase: int = 1
    min_lowercase: int = 1
    min_digits: int = 1
    min_special_chars: int = 1
    rockyou_gz_file: str = "rockyou.txt.gz"  # Default value

    def __post_init__(self):
        """Initializes the password strength checker and loads the RockYou dataset."""
        self.rockyou_passwords = set()  # Initialize an empty set to store RockYou passwords
        self.load_rockyou_dataset()  # Load the RockYou password dataset

    def load_rockyou_dataset(self):
        """
        Loads the RockYou password dataset from a compressed .gz file.

        The dataset is read and stored in the 'rockyou_passwords' set. This set is later
        used to check if a given password has been leaked in the dataset.

        Raises:
            FileNotFoundError: If the RockYou file cannot be found in the expected directory.
            Exception: If any other errors occur while loading the dataset.
        """
        try:
            # Get the directory of the current script
            base_dir = os.path.dirname(__file__)
            data_dir = os.path.join(base_dir, 'data')  # Path to the 'data' directory
            file_path = os.path.join(data_dir, self.rockyou_gz_file)  # Full path to the .gz file

            print(f"Loading RockYou dataset from {file_path}...")

            # Open and read the dataset
            with gzip.open(file_path, "rt", encoding="latin1") as rockyou:
                # Read all lines and split them into a set (one password per line)
                self.rockyou_passwords = set(rockyou.read().splitlines())
            print(f"RockYou dataset loaded with {len(self.rockyou_passwords)} passwords.")
        except FileNotFoundError:
            print(f"Error: File '{self.rockyou_gz_file}' not found in the data directory.")
        except Exception as e:
            print(f"An error occurred while loading RockYou dataset: {e}")

    def is_valid(self):
        """
        Validates the password by checking:
        1. If the password is found in the RockYou dataset (i.e., if it has been leaked).
        2. If the password meets the strength criteria.

        Returns:
            str: A message indicating whether the password is valid or has been leaked.
        """
        if self.password_in_leaked_dataset():
            return "Password has been leaked"

        # If not leaked, evaluate its strength
        strength = self.calculate_password_strength()
        return strength

    def calculate_password_strength(self):
        """
        Calculates the strength of the password based on the following criteria:
        - Minimum length
        - Minimum number of uppercase characters
        - Minimum number of lowercase characters
        - Minimum number of digits
        - Minimum number of special characters

        Returns:
            str: A message indicating the strength of the password (e.g., 'Very Weak', 'Strong').
        """
        score = 0
        password = self.password

        # Check each criterion and increment score if the condition is met
        if len(password) >= self.min_length:
            score += 1
        if sum(1 for c in password if c.isupper()) >= self.min_uppercase:
            score += 1
        if sum(1 for c in password if c.islower()) >= self.min_lowercase:
            score += 1
        if sum(1 for c in password if c.isdigit()) >= self.min_digits:
            score += 1
        if sum(1 for c in password if c in "!@#$%^&*()_+-=[]{}|;:,.<>?/~") >= self.min_special_chars:
            score += 1

        # Calculate percentage score based on the number of conditions met
        score_percentage = (score / 5) * 100

        # Return strength based on the calculated score
        if score_percentage == 0:
            return "Very Weak Password"
        elif 0 < score_percentage <= 20:
            return "Very Weak Password"
        elif 21 <= score_percentage <= 40:
            return "Weak Password"
        elif 41 <= score_percentage <= 60:
            return "Medium Password"
        elif 61 <= score_percentage <= 80:
            return "Strong Password"
        else:
            return "Very Strong Password"

    def password_in_leaked_dataset(self):
        """
        Checks if the password appears in the RockYou dataset (a set of leaked passwords).

        Returns:
            bool: True if the password is found in the dataset, False otherwise.
        """
        password = self.password.strip()  # Remove leading and trailing whitespace
        if password in self.rockyou_passwords:
            return True
        return False
