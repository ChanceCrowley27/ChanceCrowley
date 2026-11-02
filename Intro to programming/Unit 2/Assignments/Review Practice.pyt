band=input("what is the band you are going to see \n>")

num_people=float(input("how many people are going to watch them\n>"))

ticket_price=float(input("how much do the tickets cost \n>"))

total_price=(num_people*ticket_price)



def show_cost(people,band,totalprice):
    print( people +" people are going to see "+ band +" in concert and tickets will cost "+"$ "+totalprice)
show_cost(str(num_people),band,str(total_price))