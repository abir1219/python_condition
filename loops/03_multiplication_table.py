number = int(input("Enter any number: "))
total = 0
for i in range(1,11):
    if(i == 5):
        continue
    total = number * i
    print(f"{number} * {i} = {total}")