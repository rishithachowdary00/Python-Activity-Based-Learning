# Retail Billing with Multiple Discount Rules
n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    total += price * qty

discount = total * 0.10 if total >= 2000 else 0
discount = min(discount, 500)
tax = total * 0.05
bill = total - discount + tax

print("Total:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", bill)
