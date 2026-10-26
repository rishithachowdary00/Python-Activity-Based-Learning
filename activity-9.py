#Food Supply Chain Stock Reconciliation
locations = ["College", "Hostel", "Canteen"]

for place in locations:
    received = int(input("Quantity received: "))
    distributed = int(input("Quantity distributed: "))
    damaged = int(input("Quantity damaged: "))
    remaining = received - distributed - damaged

    print(place, "Remaining:", remaining)
    if remaining < 10:
        print("Replenishment needed:", 10 - remaining)
    if remaining < 0:
        print("Stock discrepancy detected")
