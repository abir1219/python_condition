num = int(input("Enter any no: "))
data = num
for i in range(2,num):
    if num % i == 0:
        print(f"{num} is not a prime no")
        break
else:
    print(f"{num} is a prime no")
