import random
Classes = ["Math", "English", "Science"]
firstname = input("What is your first name?")
lastname = input("What is your last name?")

for item in Classes:
    gpa = random.randint(255,400)/100
    if gpa<2.5:
        print ("You failed this class")
    elif gpa>=2.6 and gpa<=3.0:
        print ("You got a B")
    elif gpa>3.0:
        print ("You got an A")
    print ("First name is", firstname, "and last name is", lastname, "with class", item, "and gpa", gpa)
