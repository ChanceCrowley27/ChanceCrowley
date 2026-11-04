fruit=["apple", "grape", "strawberry","blueberry","banana"]

print(fruit[0])
print(fruit[-1])

add_fruit=input("add a fruit\n")

fruit.append(add_fruit)

print (fruit)

remove_fruit=input("remove a fruit\n")

fruit.remove(remove_fruit)

print(fruit)

fruit.sort()

print(fruit)
