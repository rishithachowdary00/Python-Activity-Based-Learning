#multi stage examination eligibility system
attendance = int(input("Enter attendance %: "))
lab = input("Lab completed (yes/no): ")
internal = int(input("Enter internal marks: "))
fees = input("Fees cleared (yes/no): ")

if attendance < 75:
    print("Attendance shortage")
if lab != "yes":
    print("Lab not completed")
if internal < 40:
    print("Internal marks insufficient")
if fees != "yes":
    print("Fees not cleared")

if attendance >= 75 and lab == "yes" and internal >= 40 and fees == "yes":
    print("Eligible for final examination")