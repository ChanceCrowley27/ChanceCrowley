item=input("item \n")

price=input("enter a price \n")

price=float(price)

rate=float(1.06875)

final_price=(price*rate)

answer=(final_price)

answer_as_string=str(answer)

price=str(price)

print("-------------------------------------------------------------")

print(item +" costs "+ price +" dollars before tax and " + answer_as_string + " after tax")

