try:
    upto = int(input("Numbers upto: "))
except Exception as e:
    print("Invalid input")
    exit()
total = 0
for num in range(1,upto+1):
    if(num%2 == 0):
        total += num
print(f"Sum of even nos upto {upto} is {total}")