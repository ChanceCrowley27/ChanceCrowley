import random

number_generator=random.randint(1,100)
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

if num_guesses == 1:
    print("Unreal")
elif num_guesses <=3:
    print("CHAMPION")
elif num_guesses <=5:
    print ("Elite")
elif num_guesses <=7:
    print("Diamond")
elif num_guesses <=9:
    print("Platinum")
elif num_guesses <=12:
    print("Gold")
elif num_guesses<=13:
    print("Silver")
elif num_guesses<=15:
    print("Bronze")
elif num_guesses <=25:
    print("Wood")
else:
    print("Failure")
    



