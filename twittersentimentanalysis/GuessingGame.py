import random
n = random.randint(1,99)
guess = int(input("Give a number between 1 and 99"))
while guess!=n:
    if guess<n:
        print ("guess is too low")
        guess = int(input("Give a number between 1 and 99"))
    elif guess > n:
        print ("guess is too high")
        guess = int(input("Give a number between 1 and 99"))
    else :
        print ("You guessed it!")
        break



