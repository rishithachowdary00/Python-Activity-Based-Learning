#Campus event financial planning
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))
sponsor = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per participant: "))
total = venue + equipment + catering + transport + certificates
shortfall = max(0, total - sponsor)
participants = int(shortfall / fee) + (shortfall % fee > 0)
print("Total Cost:", total, "\nSponsorship Shortfall:", shortfall)
print("Participant Contribution Needed:", shortfall)
print("Minimum Registrations to Break Even:", participants)