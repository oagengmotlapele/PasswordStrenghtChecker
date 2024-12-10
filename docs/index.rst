.. Password Strength Checker documentation master file, created by
   sphinx-quickstart on Mon Dec 10 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the Password Strength Checker documentation!
=======================================================

Password Strength Checker
==========================
A Python library for checking the strength of a password and verifying if it has been leaked in the RockYou dataset.

Features
--------
- **Password Strength Checker** based on custom criteria.
- **Verification** against leaked password databases (RockYou dataset).
- **Easy-to-use API** for developers.

Installation
------------
To install the Password Strength Checker, use `pip`:

.. code-block:: bash

   pip install password-strength-checker-pro

.. _attributes:

Attributes
----------

- **password** (*str*): The password to be checked.
- **min_length** (*int*): The minimum length required for the password. Default is 8.
- **min_uppercase** (*int*): The minimum number of uppercase characters required. Default is 1.
- **min_lowercase** (*int*): The minimum number of lowercase characters required. Default is 1.
- **min_digits** (*int*): The minimum number of digits required. Default is 1.
- **min_special_chars** (*int*): The minimum number of special characters required. Default is 1.
- **rockyou_gz_file** (*str*): The filename of the RockYou password dataset. Default is 'rockyou.txt.gz'.

.. _methods:

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

.. _usage:

Usage
-----
Here’s an example of how to use the Password Strength Checker:

.. code-block:: python

   from password_strength_checker import check_strength, check_leaked

   # Check password strength
   password = "P@ssw0rd123!"
   strength = check_strength(password)
   print(f"Password strength: {strength}")

   # Check if password is leaked in the RockYou dataset
   is_leaked = check_leaked(password)
   if is_leaked:
       print("This password has been leaked!")
   else:
       print("This password is safe.")

License
-------
The project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
------------
We welcome contributions to enhance the Password Strength Checker. If you would like to contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Implement the feature and add tests.
4. Submit a pull request to the main repository.

Support
-------
For support, open an issue on the GitHub repository or contact the project maintainers.

Documentation
-------------
The documentation for the Password Strength Checker is built using Sphinx. If you'd like to help improve the documentation, please refer to the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/oagengmotlapele/PasswordStrenghtChecker/contributing

Related Projects
----------------
If you are interested in password security, check out these related projects:

- **Password Leak Checker**: A tool to check passwords against various leaked databases.
- **Password Strength Meter**: A browser-based password strength meter.

Contents:
---------
* :ref:`features`
* :ref:`methods`
* :ref:`usage`
* :ref:`attributes`

Indices and Tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
