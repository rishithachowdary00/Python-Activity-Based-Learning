# Retail Billing with Multiple Discount Rules
n = int(input("Enter number of products: "))
subtotal = 0
tax_total = 0
items = []
for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    amount = price * quantity
    # Category-specific tax rates
    if category.lower() == "food":
        tax_rate = 5
    elif category.lower() == "clothing":
        tax_rate = 5
    elif category.lower() == "electronics":
        tax_rate = 18
    else:
        tax_rate = 12
    tax = amount * tax_rate / 100
    subtotal += amount
    tax_total += tax
    items.append([name, quantity, price, amount, tax])
# Threshold-based discounts
if subtotal >= 5000:
    discount_rate = 15
elif subtotal >= 3000:
    discount_rate = 10
elif subtotal >= 1000:
    discount_rate = 5
else:
    discount_rate = 0
discount = subtotal * discount_rate / 100
# Maximum concession limit
max_concession = 1000
if discount > max_concession:
    discount = max_concession
# Final bill calculation
grand_total = subtotal + tax_total - discount
# Print invoice
print("\n========== RETAIL INVOICE ==========")
print(f"{'Product':15}{'Qty':>5}{'Price':>10}{'Amount':>12}")
for item in items:
   print(f"{item[0]:15}{item[1]:>5}{item[2]:>10.2f}{item[3]:>12.2f}")
print("------------------------------------")
print(f"Subtotal             : Rs. {subtotal:.2f}")
print(f"Total Tax            : Rs. {tax_total:.2f}")
print(f"Discount ({discount_rate}%)       : Rs. {discount:.2f}")
print(f"Maximum Concession   : Rs. {max_concession:.2f}")
print("------------------------------------")
print(f"Grand Total          : Rs. {grand_total:.2f}")
print("====================================")
