# =====================================================================
# Documentation Answers (Question 1-4)
# =====================================================================
# 1. What does each function do?
#    - calculate_total(price, quantity): Multiplies the item price by 
#      the quantity purchased to return the total purchase cost.
#    - calculate_change(payment, total): Subtracts the total cost from 
#      the amount paid. If the payment is less than the total, it returns 
#      the absolute shortage amount instead of a negative value.
#
# 2. What is the difference between the parameters price and quantity 
#    and the actual arguments passed to the function?
#    - Parameters (price, quantity) are the variables defined in the 
#      function header that act as placeholders for the data the function 
#      expects to receive. Arguments are the actual values or variables 
#      passed into the function when it is called (e.g., user inputs).
#
# 3. Where is the returned total stored, and how is it reused?
#    - The returned total is stored in a variable (e.g., `total_cost`). 
#      It is reused when it is passed as an argument into the 
#      `calculate_change()` function and when printing the final cost.
#
# 4. Why is it useful to separate total calculation from change 
#    calculation?
#    - It promotes modularity, readability, and reusability. Each 
#      function has a single, clear responsibility, making the code 
#      easier to debug, test, and maintain independently.
# =====================================================================


def calculate_total(price, quantity):
    """Calculates and returns the total purchase cost.""[span_0](start_span)"[span_0](end_span)
    return price * quantity


def calculate_change(payment, total):
    """Calculates and returns the change, or handles insufficient 

    payment by returning the shortage amount.
    ""[span_1](start_span)"[span_1](end_span)
    change = payment - total
    # If payment is insufficient, display/return the additional amount needed
    if change < 0:
        return abs(change)
    return change


def main():
    # 1. Ask for the item's price, quantity, and payment[span_2](start_span)[span_2](end_span)
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    payment = float(input("Enter amount paid: "))

    # 2 & 3. Pass the price and quantity to calculate_total() and store the result[span_3](start_span)[span_3](end_span)
    total_cost = calculate_total(price, quantity)

    # 4. Pass the payment and computed total to calculate_change()[span_4](start_span)[span_4](end_span)
    change_or_shortage = calculate_change(payment, total_cost)

    # 5. Display the total cost[span_5](start_span)[span_5](end_span)
    print(f"Total Cost: PHP {total_cost:.2f}")

    # 6. Display change or shortage message depending on payment adequacy[span_6](start_span)[span_6](end_span)
    if payment < total_cost:
        print(f"Shortage: PHP {change_or_shortage:.2f}")
    else:
        print(f"Change: PHP {change_or_shortage:.2f}")


if __name__ == "__main__":
    main()

