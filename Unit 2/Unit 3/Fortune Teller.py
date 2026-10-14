import random

print("Greetings I am Swapert The GREAT\n I am here to show a fortune to you hoo hoo")
def fortune():
    try:
        Q_1=input("what is the your favorite number\n")
        random_num= random.randint(1,100)
        Q_2=input("Whats you least favorite number\n")
    except:
        print("SeE yOu SoOn")
    if int(Q_1)+(random_num)+int(Q_2)>=120:
                    print("forgot how to code did you?")
    elif int(Q_1)+(random_num)+int(Q_2)<=100:
                    print("Your riches will come soon")
    elif int(Q_1)+(random_num)+int(Q_2) <=60:
                    print("Your Shoes Untied")
    elif int(Q_1)+(random_num)+int(Q_2) <=0:
                    print("Cant SEE your Fortune Try again")

fortune()


