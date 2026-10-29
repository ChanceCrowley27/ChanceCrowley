
age=int(input("what is your age \n"))
money=float(input("how much money do you have\n"))
purchase=input("Confirm Purchase \n")
if age>=18:
       if money >=139.99:
              if purchase.lower() =="yes":
                     print("Purchase Confirmed")
elif age < 18:
    parent_permission=input("has your parent/guardian given permission\n")
    if parent_permission.lower() =="yes":
           if money >= 139.99:
                  if purchase.lower() =="yes":
                         print("purchase confirmed")
else:
     print("Purchase Denied")

