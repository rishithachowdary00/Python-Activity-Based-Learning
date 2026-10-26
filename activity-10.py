days = int(input("Enter number of days: "))
start = int(input("Starting weekday (0=Mon, 6=Sun): "))

print("Mon Tue Wed Thu Fri Sat Sun")
for i in range(start):
    print("    ", end="")

for day in range(1, days + 1):
    print(f"{day:3}", end=" ")
    if (start + day) % 7 == 0:
        print()
