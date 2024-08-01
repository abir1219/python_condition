pet = input("What is your pet? ")
age = int(input("What is your pet age? "))
if(pet == "Dog" and age < 2):
    print("Puppy food")
elif(pet == "Cat" and age > 5):
    print("Senior cat food")
else:
    print("Any thing")
