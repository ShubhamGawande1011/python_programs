basic_salary = int(input("Enter the basic salary of the employee ; "))
DA = 0.20 * basic_salary
HRA = 0.25 * basic_salary
gross_salary = basic_salary + DA + HRA

print(f"the gross salary of the employee is {gross_salary}")
