number = int(input("Enter any no : "))
factNo = number
result = 1
# for num in reversed(range(1,number)):
#     result += result * num
#     print(f"Num = {num} and result = {result}")

while factNo > 0:
    result *= factNo
    factNo -=1
print(f"Factorial of {number} is {result}")