# Energy conservation before and after analysis
before = int(input("Usage before: "))
after = int(input("Usage after: "))
saved = before - after
print("Units saved:", saved)
if before > 0:
    percent = saved / before * 100
    print("Percentage saved:", percent)
else:
    print("Cannot calculate percentage")