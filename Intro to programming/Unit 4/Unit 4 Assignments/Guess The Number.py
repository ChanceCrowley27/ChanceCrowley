import random

number_generator=random.randint(1,101)
guess=False
num_guesses=0
while guess==False:
    guess=input("guess the number between 1 and 100\n>")\
    
    num_guesses+=1

    if int(guess)==number_generator:
        print("You guessed the number")
        guess==True
        print("you guessed in "+str(num_guesses)+" attempts")


    elif int(guess)>number_generator:
        print("Your number is lower than the one you guessed")
        guess=False

    elif int(guess)<number_generator:
        print("Your number is higher than the one you guessed")
        guess=False
    
    else:
        guess= False
    



