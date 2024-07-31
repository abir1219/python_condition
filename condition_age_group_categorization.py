age = int(input("Enter age : "))
if(age < 13):
    print("The person is a child")
elif(age >= 13 and age <= 19):
    print("The person is a teenager")
elif(age >= 20 and age <= 59):
    print("The person is an adult")
elif(age >= 60):
    print("The person is a senior citizen")