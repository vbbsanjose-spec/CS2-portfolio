def multiply_num(price, quantity):
  magkano_lahat = price * quantity
  return magkano_lahat

def subtract_num(payment, total_cost):
  if payment >= total_cost:
    return payment - total_cost
  else:
    return total_cost - payment
  
price = float(input("How much is the item?:"))
quantity = int(input("How many do you want to buy?:"))
payment = float(input("Enter amount you want to give:"))

total_cost = multiply_num(price, quantity)
change = subtract_num(payment, total_cost)

print("The total cost is", total_cost)

if payment >= total_cost:
  print("Your change is", change)

else:
  print("Your shortage amount is", change)

  

