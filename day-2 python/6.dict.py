#written in curly brackets
#stores key-value pairs
#key is unique, value can be duplicate

my_dict={"name":"John", "age":30, "city":"New York"}
print("Dictionary:", my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print("name:", my_dict["name"])  # Accessing value by key
print("age:", my_dict["age"])  # Accessing value by key
my_dict["age"] = 31  # Updating value
print("Updated Dictionary:", my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}
my_dict["country"] = "USA"  # Adding a new key-value pair
print("Dictionary after adding country:", my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}
print("keys:", my_dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'country'])
print("values:", my_dict.values())  # Output: dict_values(['John', 31, 'New York', 'USA'])
print("items:", my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 31), ('city', 'New York'), ('country', 'USA')])
print("length of dictionary:", len(my_dict))  # Output: 4
print("check if key exists:", "name" in my_dict)  # Output: True

my_dict.pop("age")  # Removing a key-value pair
print("Dictionary after removing age:", my_dict)  # Output: {'name': 'John', 'city': 'New York', 'country': 'USA'}
my_dict.popitem()# Removing the last inserted key-value pair
print("Dictionary after removing last item:", my_dict)  # Output: {'name': 'John', 'city': 'New York'}

#for loop
for key in my_dict:
    print(key, ": ", my_dict[key]) 