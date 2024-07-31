score = int(input("Enter score : "))
if(score > 100 or score < 0):
    print("Enter a valid score")
else:
    if(score >= 90 and score <= 100):
        print("Grade : A")
    elif(score >= 70 and score <= 89):
        print("Grade : B")
    elif(score >= 70 and score <= 79):
        print("Grade : C")
    elif(score >= 60 and score <= 69):
        print("Grade : D")
    elif(score < 60):
        print("Grade : F")     