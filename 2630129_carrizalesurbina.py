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
# A list is an ordered mutable collection. A tuple is ordered
# but immutable. A dictionary stores key-value pairs for fast
# lookup by key. Lists can grow or shrink; tuples cannot change
# after creation. Dictionaries associate a key with a value.
# This file covers six problems using lists, tuples and dicts
# with description, inputs, outputs, validations and test cases.
# ============================================================

# ============================================================
# PRINCIPLES AND BEST PRACTICES
# ============================================================
# Use lists when you need to add or remove elements.
# Use tuples for data that must not change.
# Use dictionaries for fast lookup by key.
# Avoid modifying a list while iterating with for.
# Use descriptive key names. Write clear messages.
# ============================================================

# ============================================================
# PROBLEM 1: Shopping list basics (list operations)
# ============================================================
# Description: Create a list from products, append a new item,
# show total items and check if an item exists.
#
# Inputs (fixed):
#   initial_items_text = "apple,banana,orange"
#   new_item = "mango"
#   search_item = "banana"
# Outputs: "Items list:", "Total items:", "Found item:"
# Validations: non-empty strings, remove extra spaces
#
# Test cases:
# 1) Normal: "apple,banana,orange" + "mango" + "banana"
# 2) Border: "  apple  " + "kiwi" + "apple"
# 3) Error: empty string
# ============================================================

print("=== Problem 1 ===")
initial_items_text = "apple,banana,orange"
new_item = "mango"
search_item = "banana"

items_list = [item.strip() for item in initial_items_text.split(",")]
items_list.append(new_item)
print("Items list:", items_list)
print("Total items:", len(items_list))
print("Found item:", search_item in items_list)

# ============================================================
# PROBLEM 2: Points and distances with tuples
# ============================================================
# Description: Create two points as tuples, calculate Euclidean
# distance and midpoint.
#
# Inputs (fixed): x1=0, y1=0, x2=3, y2=4
# Outputs: "Point A:", "Point B:", "Distance:", "Midpoint:"
# Validations: values are floats
#
# Test cases:
# 1) Normal: 0 0 3 4
# 2) Border: same point
# 3) Error: non-numeric
# ============================================================

print("\n=== Problem 2 ===")
x1 = 0.0
y1 = 0.0
x2 = 3.0
y2 = 4.0

point_a = (x1, y1)
point_b = (x2, y2)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2)/2, (y1 + y2)/2)

print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", round(distance, 4))
print("Midpoint:", midpoint)

# ============================================================
# PROBLEM 3: Product catalog with dictionary
# ============================================================
# Description: Catalog with product name as key and price as value.
# Calculate total for a given product and quantity.
#
# Inputs (fixed): product_name="apple", quantity=3
# Outputs: "Unit price:", "Quantity:", "Total:"
# Validations: non-empty name, quantity > 0, key exists
#
# Test cases:
# 1) Normal: "apple" 3
# 2) Border: "banana" 1
# 3) Error: "xyz"
# ============================================================

print("\n=== Problem 3 ===")
product_prices = {"apple": 10.0, "banana": 5.5, "orange": 8.0}
product_name = "apple"
quantity = 3

unit_price = product_prices[product_name]
total = unit_price * quantity
print("Unit price:", unit_price)
print("Quantity:", quantity)
print("Total:", round(total, 2))

# ============================================================
# PROBLEM 4: Student grades with dict and list
# ============================================================
# Description: Dictionary of student name to list of grades.
# Calculate average and whether the student passed (>= 70).
#
# Inputs (fixed): student_name="Alice"
# Outputs: "Grades:", "Average:", "Passed:"
# Validations: name exists, grades list not empty
#
# Test cases:
# 1) Normal: "Alice"
# 2) Border: "Bob"
# 3) Error: "Unknown"
# ============================================================

print("\n=== Problem 4 ===")
grades = {
    "Alice": [90.0, 85.0, 78.0],
    "Bob": [70.0, 70.0, 70.0],
    "Carol": [55.0, 60.0, 65.0]
}
student_name = "Alice"

grades_list = grades[student_name]
average = sum(grades_list) / len(grades_list)
is_passed = average >= 70.0
print("Grades:", grades_list)
print("Average:", round(average, 2))
print("Passed:", is_passed)

# ============================================================
# PROBLEM 5: Word frequency counter (list + dict)
# ============================================================
# Description: Split a sentence into words, count frequency with
# a dictionary and show the most common word.
#
# Inputs (fixed): sentence = "the cat and the dog and the cat"
# Outputs: "Words list:", "Frequencies:", "Most common word:"
# Validations: non-empty sentence
# Decision: remove simple punctuation with replace()
#
# Test cases:
# 1) Normal: "the cat and the dog and the cat"
# 2) Border: "hello"
# 3) Error: empty
# ============================================================

print("\n=== Problem 5 ===")
sentence = "the cat and the dog and the cat"
cleaned = sentence.lower()
words_list = cleaned.split()
freq_dict = {}
for word in words_list:
    freq_dict[word] = freq_dict.get(word, 0) + 1
most_common_word = max(freq_dict, key=freq_dict.get)
print("Words list:", words_list)
print("Frequencies:", freq_dict)
print("Most common word:", most_common_word)

# ============================================================
# PROBLEM 6: Simple contact book (dictionary CRUD)
# ============================================================
# Description: Mini contact book demonstrating ADD, SEARCH, DELETE.
#
# Inputs (fixed):
#   ADD: name="David", phone="5550001111"
#   SEARCH: name="Alice"
#   DELETE: name="Bob"
# Outputs: according to each action
# Validations: valid action, non-empty name/phone
#
# Test cases:
# 1) Normal ADD
# 2) Border SEARCH
# 3) Error DELETE
# ============================================================

print("\n=== Problem 6 ===")
contacts = {"Alice": "5551234567", "Bob": "5559876543"}

# ADD
name = "David"
phone = "5550001111"
contacts[name] = phone
print("Contact saved:", name, phone)

# SEARCH
name = "Alice"
print("Phone:", contacts.get(name))

# DELETE
name = "Bob"
contacts.pop(name)
print("Contact deleted:", name)

# ============================================================
# CONCLUSIONS
# ============================================================
# Lists are best when elements need to be added or removed.
# Tuples are useful for fixed data that must not change.
# Dictionaries allow fast searches by key.
# Combining dict of lists is a common pattern (student grades).
# Always validate inputs before processing.
# ============================================================

# ============================================================
# REFERENCES
# ============================================================
# 1) Python docs - Built-in Types: list, tuple, dict
#    https://docs.python.org/3/library/stdtypes.html
# 2) Python Tutorial - Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Real Python - Lists and Tuples
#    https://realpython.com/python-lists-tuples/
# 4) Real Python - Dictionaries
#    https://realpython.com/python-dicts/
# 5) Lutz, M. Learning Python. O'Reilly.
# ============================================================
