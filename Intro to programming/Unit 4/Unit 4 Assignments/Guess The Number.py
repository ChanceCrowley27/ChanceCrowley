import random

number_generator=random.randint(1,100)
guess=False

while guess==False:
    guess=input("guess the number between 1 and 100\n>")

    if int(guess)==number_generator:
        print("You guessed the number")
        guess==True

    elif int(guess)>number_generator:
        print("Your number is lower than the one you guessed")
        guess=False

    elif int(guess)<number_generator:
        print("Your number is higher than the one you guessed")
        guess=False
    
    else:
        guess= False
    



