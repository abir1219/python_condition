age = int(input("What is your age: "))
total = 0
if(age < 18):
    total += 8
elif(age >= 18):
    total += 12
day = input("What is the day today? ")
if(day == "Wednesday"):
    total = total - 2

print("Total Price : ₹"+str(total))