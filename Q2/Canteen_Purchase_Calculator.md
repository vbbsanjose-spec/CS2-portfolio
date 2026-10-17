
# Documentation Answers (Question 1-4)

# 1. What does each function do?
 CalculateTotal(price, quantity): Multiplies the item price by the quantity purchased to return the total purchase cost.
      
CalculateChange(payment, total): Subtracts the total cost from the amount paid. If the payment is less than the total, it returns the absolute shortage amount instead of a negative value.

# 2. What is the difference between the parameters price and quantity 
    and the actual arguments passed to the function?
    - Parameters (price, quantity) are the variables defined in the 
     function header that act as placeholders for the data the function 
     expects to receive. Arguments are the actual values or variables 
     passed into the function when it is called (e.g., user inputs).

# 3. Where is the returned total stored, and how is it reused?
    - The returned total is stored in a variable (e.g., `total_cost`). 
      It is reused when it is passed as an argument into the 
      `calculate_change()` function and when printing the final cost.

# 4. Why is it useful to separate total calculation from change calculation?
    - It promotes modularity, readability, and reusability. Each function has a single, clear responsibility, making the code easier to debug, test, and maintain independently.

------
'''python

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

'''
------
