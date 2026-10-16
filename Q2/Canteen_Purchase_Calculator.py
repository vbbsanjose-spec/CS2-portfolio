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
    
