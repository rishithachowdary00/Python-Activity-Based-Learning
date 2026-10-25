# Examination seating
rows = 7
cols = 4

for i in range(rows):
    for j in range(cols):
        if (i, j) == (1, 1):
            print("Reserved", end="\t")
        elif (i + j) % 2 == 0:
            print(f"R{i+1}C{j+1}", end="\t")
        else:
            print("--", end="\t")
    print()