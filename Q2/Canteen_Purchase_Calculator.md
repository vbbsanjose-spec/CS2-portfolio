
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

'''python

def calculate_total(price, quantity):
   return price * quantity


def calculate_change(payment, total):
    return payment - total


# Ask for item inputs
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

# Calculate total and change
total_cost = calculate_total(price, quantity)
change = calculate_change(payment, total_cost)

# Display results
print(f"Total Cost: PHP {total_cost:.2f}")

if change < 0:
    print(f"Shortage: PHP {abs(change):.2f}")
else:
    print(f"Change: PHP {change:.2f}")

'''
