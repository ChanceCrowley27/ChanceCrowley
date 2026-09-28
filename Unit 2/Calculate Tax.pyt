your_item=input("what are you buying \n")
item_price=float(input("how much does that item cost \n"))
tax_rate=1.06875

def calculate_tax(item, price, rate):
    print(item + " costs $"+ str(price) + " before tax and "+str(round(item_price*rate,2))+ " after tax.")

calculate_tax(your_item, item_price, tax_rate)
