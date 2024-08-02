str = input("Enter any string : ")
for char in str:
    if(str.count(char) == 1):
        print(f"The non repeated character is : {char}")
        break