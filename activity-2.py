basic = float(input("Enter basic salary: "))
allow = float(input("Enter allowances: "))
ot = float(input("Enter overtime: "))
bonus = float(input("Enter incentives: "))
gross = basic + allow + ot + bonus
tax = gross * 0.05 if gross <= 20000 else gross * 0.10
pf = basic * 0.12
deduction = tax + pf
net = gross - deduction
print("Gross:", gross, "Deductions:", deduction, "Net Salary:", net)
