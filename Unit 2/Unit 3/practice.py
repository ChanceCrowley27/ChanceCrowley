def mult():
    num_one=input("give a number\n")
    num_two=input("give another number\n")
    try:
        print(float(num_one)*float(num_two))
    except:
        print("invalid input. try again")
        mult()
mult()
