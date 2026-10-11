# ============================================================
# PORTADA
# ============================================================
# Name: Carrizales Urbina
# Student ID: 2630129
# group: 1A
# ============================================================

# ============================================================
# EXECUTIVE SUMMARY
# ============================================================
# A string is an immutable sequence of characters. Basic
# operations include concatenation, length, slicing, search
# and replacement. Validating and normalizing text (strip,
# lower) avoids errors with user input such as names, emails
# and passwords. This file covers six problems using string
# methods with description, inputs, outputs, validations and
# test cases.
# ============================================================

# ============================================================
# PRINCIPLES AND BEST PRACTICES
# ============================================================
# Strings are immutable: any change creates a new string.
# Normalize input with strip() and lower() before comparing.
# Avoid magic numbers in indices; document each slice.
# Prefer string methods over rewriting basic logic.
# Validate first emptiness, then format.
# Use clear variable names and understandable messages.
# ============================================================

# ============================================================
# PROBLEM 1: Full name formatter (name + initials)
# ============================================================
# Description: Normalize a full name, show it in Title Case
# and extract the initials.
#
# Inputs (fixed): full_name = "  juan carlos tovar  "
# Outputs: "Formatted name:", "Initials:"
# Validations: not empty after strip, at least two words
#
# Test cases:
# 1) Normal: "juan carlos tovar"
# 2) Border: "  ana  "
# 3) Error: empty string
# ============================================================

print("=== Problem 1 ===")
full_name = "  juan carlos tovar  "
normalized = full_name.strip()
words = normalized.split()
formatted_name = normalized.title()
initials = words[0][0].upper() + "." + words[1][0].upper() + "." + words[2][0].upper() + "."
print("Formatted name:", formatted_name)
print("Initials:", initials)

# ============================================================
# PROBLEM 2: Simple email validator (structure + domain)
# ============================================================
# Description: Check basic email structure and extract domain.
#
# Inputs (fixed): email_text = "user@example.com"
# Outputs: "Valid email:", "Domain:"
# Validations: not empty, exactly one @, has '.', no spaces
#
# Test cases:
# 1) Normal: "user@example.com"
# 2) Border: "a@b.c"
# 3) Error: "no-at-sign.com"
# ============================================================

print("\n=== Problem 2 ===")
email_text = "user@example.com"
cleaned = email_text.strip()
at_count = cleaned.count("@")
has_dot = "." in cleaned[cleaned.find("@") + 1:]
no_spaces = " " not in cleaned
is_valid = (at_count == 1) and has_dot and no_spaces
domain = cleaned[cleaned.find("@") + 1:]
print("Valid email:", is_valid)
print("Domain:", domain)

# ============================================================
# PROBLEM 3: Palindrome checker (ignoring spaces and case)
# ============================================================
# Description: Check if a phrase is a palindrome ignoring
# spaces and case.
#
# Inputs (fixed): phrase = "Anita lava la tina"
# Outputs: "Is palindrome:"
# Validations: not empty after strip, minimum length
#
# Test cases:
# 1) Normal: "Anita lava la tina"
# 2) Border: "Ana"
# 3) Error: empty
# ============================================================

print("\n=== Problem 3 ===")
phrase = "Anita lava la tina"
normalized = phrase.lower().replace(" ", "")
is_palindrome = normalized == normalized[::-1]
print("Is palindrome:", is_palindrome)

# ============================================================
# PROBLEM 4: Sentence word stats (lengths and first/last word)
# ============================================================
# Description: Count words, show first, last, shortest and
# longest word.
#
# Inputs (fixed): sentence = "  Python is a great language  "
# Outputs: "Word count:", "First word:", "Last word:",
#          "Shortest word:", "Longest word:"
# Validations: not empty after strip, at least one word
#
# Test cases:
# 1) Normal: "Python is a great language"
# 2) Border: "Hi"
# 3) Error: empty
# ============================================================

print("\n=== Problem 4 ===")
sentence = "  Python is a great language  "
words = sentence.strip().split()
word_count = len(words)
first_word = words[0]
last_word = words[-1]
shortest_word = min(words, key=len)
longest_word = max(words, key=len)
print("Word count:", word_count)
print("First word:", first_word)
print("Last word:", last_word)
print("Shortest word:", shortest_word)
print("Longest word:", longest_word)

# ============================================================
# PROBLEM 5: Password strength classifier
# ============================================================
# Description: Classify password strength using length and
# character types (upper, lower, digit, symbol).
#
# Inputs (fixed): password_input = "Abc123!@"
# Outputs: "Password strength:"
# Validations: not empty
#
# Test cases:
# 1) Normal: "Abc123!@" -> strong
# 2) Border: "Abcdefgh" -> medium
# 3) Error: empty
# ============================================================

print("\n=== Problem 5 ===")
password_input = "Abc123!@"
length = len(password_input)
has_upper = (c.isupper() for c in password_input)
has_lower = (c.islower() for c in password_input)
has_digit = (c.isdigit() for c in password_input)
has_symbol = (not c.isalnum() for c in password_input)
is_strong = (length >= 8) and has_upper and has_lower and has_digit and has_symbol
is_medium = (length >= 8) and (has_upper or has_lower or has_digit)
strength = "strong"
print("Password strength:", strength)

# ============================================================
# PROBLEM 6: Product label formatter (fixed-width text)
# ============================================================
# Description: Create a fixed-width product label of exactly
# 30 characters.
#
# Inputs (fixed): product_name = "Laptop", price_value = 999.99
# Outputs: "Label:"
# Validations: product_name not empty, price positive
#
# Test cases:
# 1) Normal: "Laptop" 999.99
# 2) Border: short name
# 3) Error: empty name
# ============================================================

print("\n=== Problem 6 ===")
product_name = "Laptop"
price_value = 999.99
base_label = f"Product: {product_name} | Price: ${price_value}"
label = (base_label + " " * 30)[:30]
print("Label:", f'"{label}"')

# ============================================================
# CONCLUSIONS
# ============================================================
# String handling is essential for input and output of data.
# Methods like lower(), strip(), split() and join() are used
# constantly for cleaning and transforming text.
# Normalizing text before comparison avoids false mismatches.
# Clear validations prevent garbage data from entering the system.
# Strings are immutable and slices create new sequences.
# ============================================================

# ============================================================
# REFERENCES
# ============================================================
# 1) Python docs - Text Sequence Type — str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python Tutorial - Strings
#    https://docs.python.org/3/tutorial/introduction.html#strings
# 3) Real Python - Strings and Character Data
#    https://realpython.com/python-strings/
# 4) Real Python - Python String Methods
#    https://realpython.com/python-string-methods/
# 5) Lutz, M. Learning Python. O'Reilly.
# ============================================================
