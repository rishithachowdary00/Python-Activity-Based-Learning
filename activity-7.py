# academic progression
marks = int(input("Enter semester marks: "))
attendance = int(input("Enter attendance %: "))
prereq = input("Prerequisites completed (yes/no): ")

if marks < 40:
    print("Subject not passed")
if attendance < 75:
    print("Attendance shortage")
if prereq != "yes":
    print("Prerequisites incomplete")

if marks >= 40 and attendance >= 75 and prereq == "yes":
    print("Eligible for progression")