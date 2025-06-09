#Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary

def showEmployee(name, salary = 9000):
    return f"Name: {name} , Salary: {salary}"

print(showEmployee("Ben", 1200))
print(showEmployee("Jessa"))