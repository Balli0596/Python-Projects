import random
guess=0
print("welcome to guess game")
number=int(input("Enter a number"))
if(number<0):
    print("PLease enter a number greate than 0")
    quit()
random_number=random.randint(0,number)
while True:
    guess+=1
    User_guess=int(input("enter your number\n"))
    if(random_number==User_guess):
        print("You got it correct")
        print("you took ",guess,"guesses")
        break

    else:
        print("make another guess")
  