.. Password Strength Checker documentation master file, created by
   sphinx-quickstart on Mon Dec 10 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: methods.rst

Methods
-------

- **load_rockyou_dataset**:
    Loads the RockYou dataset from a compressed `.gz` file. This method reads the dataset from the specified file and stores the passwords in a set for future lookup.

- **is_valid**:
    Checks whether the password meets the strength criteria and if it is found in the RockYou dataset. It returns a message indicating whether the password is valid or has been leaked.

- **calculate_password_strength**:
    Calculates the strength of the password based on predefined criteria: minimum length, uppercase letters, lowercase letters, digits, and special characters. Returns a strength level message based on the score.

- **password_in_leaked_dataset**:
    Checks if the password is present in the RockYou dataset of leaked passwords. Returns `True` if the password is found in the dataset, `False` otherwise.
