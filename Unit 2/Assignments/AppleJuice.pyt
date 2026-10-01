num_apples=float(input("how many apples are you using \n>"))
num_people=float(input("what is the number of people you want \n>"))

def portion(a, p):
    return(a/p)

apples_per_person=print(portion(num_apples, num_people))

def serve(people, apples_per_person):
    print("served " + people + " a glass of apple juice at " + apples_per_person +" per glass.")

serve(people, apples)