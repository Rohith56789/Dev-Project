# Example of a tuple in Python

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuples are immutable, so you cannot modify them
# my_tuple[0] = 10  # This will raise a TypeError

# Tuples can contain mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# Tuples can be nested
nested_tuple = (1, (2, 3), (4, 5))
print("Nested tuple:", nested_tuple)

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)