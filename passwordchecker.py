#checking your password to see how many characters long 

username = input("Enter your username: ")
password = input("Enter your password: ")
print(f"{username}, your {'*' * len(password)} is \n{len(password)} characters long")
