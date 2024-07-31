age = int(input("Enter age : "))
if(age < 13):
    print("The person is a child")
elif(age <= 19):
    print("The person is a teenager")
elif(age <= 59):
    print("The person is an adult")
else:
    print("The person is a senior citizen")