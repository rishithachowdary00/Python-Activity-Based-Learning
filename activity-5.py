# Bus passenger occupancy
passengers = 0

for stop in range(3):
    board = int(input("Passengers boarding: "))
    leave = int(input("Passengers leaving: "))

    passengers = passengers + board - leave

print("Total passengers:", passengers)