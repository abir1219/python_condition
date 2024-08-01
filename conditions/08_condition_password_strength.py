password = input("Enter the password: ")
length = len(password)
if(length < 6):
    print("gPassword is weak")
elif(length < 10):
    print("Password is medium")
else:
    print("Password is strong")