def add(x, y):
    num1 = x + y
    num2 = x * y
    return num1 + num2

print(add(10, 20)) 

# Login function that checks for valid credentials
def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    else:
        return False
uname = input("Enter username: ")  # e.g. admin
password = input("Enter password: ")  # e.g. admin123

# Calling the login function and printing the result
if login(uname, password):
    print("Login successful")
else:
    print("Login failed")
