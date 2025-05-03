#no duplicates
#written in curly brackets
#unordered (no index) pops a random element 
#no mutability (cannot change an element)

my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)  # Output: {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element
print("Set after adding 6:", my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.remove(3)  # Removing an element
print("Set after removing 3:", my_set)  # Output: {1, 2, 4, 5, 6}
print('remove last element:', my_set.pop(), "removed")  # Removing and returning an arbitrary element
print("Set after pop:", my_set)  # Output: {1, 2, 4, 5}