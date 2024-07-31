score = int(input("Enter score : "))
grade = ""
if(score > 100 or score < 0):
    print("Enter a valid score")
    exit() # to exit from program
else:
    if(score >= 90):
        grade = 'A'
    elif(score >= 80):
        grade = 'B'
    elif(score >= 70):
        grade = 'C'
    elif(score >= 60):
        grade = 'D'
    else:
        grade = 'F'

print("Grade is ",grade) 