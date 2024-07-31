age = int(input("What is your age: "))

price = 12 if age > 18 else 8

# if(age < 18):
#     total += 8
# elif(age >= 18):
#     total += 12
day = input("What is the day today? ")
if(day == "Wednesday"):
    price -= 2

print("Total Price : ₹",price)