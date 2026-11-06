import random
x=0

while x <10:
    print(x)
    x +=1

buy_another=True
spent=0

while buy_another:
    spent+= 5
    print("You purchased another crate!\n-$10\n")

    roll = random.random()

    if roll <0.40:
        print("You got a green...")

    elif roll <0.75:
        print("You got a blue....")

    elif roll <0.95:
        print("You got a purple!")

    else:
        print("GOOOOOOOOOOOOOOOOOOOOLD")

    choice=input("Do you want to by another crate\ny/n\n")

    if choice=="y":
        buy_another==True

    else:
        buy_another==False