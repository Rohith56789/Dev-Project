# Demonstrating properties of a Python list: ordered, mutable, and allows duplicates

# Ordered: Elements maintain their insertion order
my_list = [10, 20, 30, 40 , 50]
print("Ordered List:", my_list)

# Mutable: Elements can be changed after creation
mutable_list = [1, 2, 3, 4]
mutable_list[2] = 99  # Changing the third element
print("Mutable List:", mutable_list)

# Allows duplicates: Lists can contain duplicate elements
duplicate_list = [5, 5, 10, 10, 15]
print("List with Duplicates:", duplicate_list)

my_list[3]  = 100  # Changing the fourth element
print("Updated List:", my_list)
my_list.insert(2, 25)  # Inserting 25 at index 2
print("List after Insertion:", my_list)