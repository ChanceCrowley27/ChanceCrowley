
try:
    wind_speed=int(input("what is the speed of the wind\n>"))
    if wind_speed <=74:
        print("Tropical Storm")
    elif wind_speed <=96:
        print("Category 1")
    elif wind_speed <=111:
        print("Category 2")
    elif wind_speed <=130:
        print("Category 3")
    elif wind_speed <=157:
        print("Category 4")
    elif wind_speed >=157:
        print("Category 5")
except:
    print("Invalid Input. Try Again")




