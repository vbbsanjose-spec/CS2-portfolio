# ~~~~ Problem Description ~~~~
The school canteen needs a simple program to calculate the total cost of a purchase and the customers
change. Create a program that asks the user to enter the price of an item, the quantity purchased and
the amount paid.


# ~~~~ Documentation Answers ~~~~

## 1. What does each function do?
multiply_num(price, quantity): Multiplies the item price by the quantity purchased to return the total purchase cost.
      
subtract_num(payment, total_cost): Subtracts the total cost from the amount paid. If the payment is less than the total, it returns the shortage amount instead of a negative value.

## 2. What is the difference between the parameters price and quantity and the actual arguments passed to the function?
Parameters are variables in the function. Actual arguments are the values passed to the function.

## 3. Where is the returned total stored, and how is it reused?
The total is stored in total_cost. It is used to calculate the change or shortage.

## 4. Why is it useful to separate total calculation from change calculation?
It makes the program easier to understand, organize, and fix because every function has its own purpose. 



# ~~~~ FINAL CODE ~~~~
```python
# The Canteen Purchase Calculator

# Making the functions
def multiply_num(price, quantity):
  magkano_lahat = price * quantity
  return magkano_lahat

def subtract_num(payment, total_cost):
  if payment >= total_cost:
    return payment - total_cost
  else:
    return total_cost - payment

# Ask for the values  
price = float(input("How much is the item?:"))
quantity = int(input("How many do you want to buy?:"))
payment = float(input("Enter amount you want to give:"))

# Using the following variables for the functions that we made earlier
total_cost = multiply_num(price, quantity)
change = subtract_num(payment, total_cost)

# Displaying the final and calculated values
print("The total cost is", total_cost)

if payment >= total_cost:
  print("Your change is", change)

else:
  print("Your shortage amount is", change)

```

