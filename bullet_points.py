"""
Script to add bullet points to each line of text from the clipboard.
"""

import pyperclip

# Get text from clipboard
text = pyperclip.paste()

# Add bullet points
lines = text.split('\n')
bulleted = '\n'.join(f'* {line}' for line in lines if line.strip())

# Copy modified text back to clipboard
pyperclip.copy(bulleted)

print("Bullet points added and copied to clipboard!")
