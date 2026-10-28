
employee = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
transport = float(input("Enter transport allowance: "))
food = float(input("Enter food allowance: "))
gross_salary = basic_salary + transport + food
print("EMPLOYEE PAYSLIP")

print(f"Employee: {employee}\n")
print(f"{'Basic Salary:'} {basic_salary} ETB")
print(f"{'Transport Allowance:'} {transport} ETB")
print(f"{'Food Allowance:'} {food} ETB")
print(f"{'Gross Salary:'} {gross_salary} ETB")
