.. Password Strength Checker documentation master file, created by
   sphinx-quickstart on Mon Dec 10 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

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


.. include:: usage.rst



Indices and Tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

