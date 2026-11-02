score=0

def tally_score():
    global score
    if score> 3:
        print ("pass")
    else:
        print("fail")

Question_1=input("what was the first MCU movie\n")

Question_2=input("what is the name of the villian in LOTR\n")

Question_3=input("what is the most expensive magic the gathering card\n")

Question_4=input("what is Chase Dallin's favorite video game\n")

Question_5=input("what is the story dune,starwars, and harrypotter ripsoff\n")

if Question_1=="Ironman":
    score = score + 1
    print("correct")
else:
    print("incorrect")



if Question_2=="Sauron":
    score = score + 1
    print("correct"); 
else:
    print("incorrect")



if Question_3=="The One Ring":
    score = score + 1
    print("correct"); score+1
else:
    print("incorrect")


if Question_4=="Super smash bros. Ultimate":
    score = score + 1
    print("correct"); score+1
else:
    print("incorrect")


if Question_5=="Lord of the Rings":
    score = score + 1
    print("correct"); score+1
else:
    print("incorrect")

print("--------------------------------------------------------------------")
tally_score()