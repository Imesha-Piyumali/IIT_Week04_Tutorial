# Coffee ordering program

print("Welcome to the Coffee Shop!")

# Ask customer name
customer_name = input("What is your name? ")

# Greet customer
print("Hello, " + customer_name + "! Let's order some coffee.")

# Ask if student
is_student = input("Are you a student? (yes/no): ").lower()

# Set discount if student
discount = 0.10 if is_student == "yes" else 0.0

total = 0.0

# Loop for orders
while True:
    coffee_price = 5.0  # base price of one coffee
    order = input("Would you like to order a coffee? (yes/no): ").lower()

    if order == "no":
        break

    elif order == "yes":
        total += coffee_price
        print("One coffee added to your order! ($5.00)")

    else:
        print("Please answer with 'yes' or 'no'.")

# Apply discount if student
if discount > 0:
    total = total - (total * discount)
    print("Student discount applied (10%).")

# Final bill
print("Thank you, " + customer_name + "!")
print("Your total bill is: $" + str(round(total, 2)))
