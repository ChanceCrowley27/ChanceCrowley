student_data={
    "Seth": "F",
    "Chase":"A++",
    "Dane":"A",
    "Matt":"A"
}

for key in student_data:
    print(key+" : "+student_data[key])
print("\n-------------------------------------------------\n")
Alice_data={
    "name":"Alice",
    "age":16,
    "grade":"A"
}

print("This girls name is "+Alice_data["name"]+"and her age is "+str(Alice_data["age"]))

Alice_data["grade"]="A+"

for key in Alice_data:
    print(key+" : "+str(Alice_data[key]))

print("\n-----------------------\n")

fav_movies={
    "Star wars a new hope": 1977,
    "Avengers: Age of Ultron":2015,
    "Sonic the Hedgehog 3":2024
}

fav_movies["Dune: Part Two"]=2024

for key in fav_movies:
    print(key+" : "+str(fav_movies[key]))

print("\n--------------------------------------------------\n")

fruit_prices={
    "apples": 7,
    "bananas": 5,
    "orange": 6,
    "grape": 10,
    "durian": 45
}

for key in fruit_prices:
    print(key+" : "+str(fruit_prices[key]))\

print("\n----------------------------------------\n")

remove_fruit=input("what fruit do you wish to remove\n>")

print("\n-----------------------\n")

del fruit_prices[remove_fruit]

for key in fruit_prices:
    print(key+" : "+str(fruit_prices[key]))

print("\n----------------------------------------------\n")

fruit_inventory={
    "apples":10,
    "bananas":5,
    "oranges": 8
}

for key in fruit_inventory:
    print(key+" : "+str(fruit_inventory[key]))