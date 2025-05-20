"""
Demo password manager
User enters an account name and the program gets the password and copies it to clipboard.
If the account is not found, the user can paste a new password to store and copy it.
"""

import pyperclip

# A simple dictionary to simulate stored passwords
passwords = {
    'email': 'EmailPass123!',
    'facebook': 'FbStrongPass456!',
    'github': 'GitSecure789!'
}

# Ask the user for the account name
account = input('Enter the account name: ').lower()

# Retrieve and copy the password if the account exists
if account in passwords:
    pyperclip.copy(passwords[account])
    print(f"Password for '{account}' has been copied to clipboard.")
else:
    print(f"No password found for account: '{account}'.")
    new_password = input("Please paste or enter a new password to save: ")
    
    if new_password.strip():
        passwords[account] = new_password
        pyperclip.copy(new_password)
        print(f"New password for '{account}' saved and copied to clipboard.")
    else:
        print("No password entered. Nothing was saved.")
