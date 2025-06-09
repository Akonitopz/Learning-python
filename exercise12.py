#Calculate income tax for the given income by adhering to the rules below:
# first 10000 has 0% tax
# next 10000 has 10% tax
# the remaining will have 20% tax
taxnum = float(input("Please enter your annual income: "))
if taxnum <= 10000:
    print("Your income is not taxable.")
else:
    con2 = 10000 * 10 / 100
    con3 = (taxnum - 20000) * 20 /100
    income_tax = + con2 + con3
    net_income = taxnum - income_tax
    
print("Your total income tax is:" , income_tax)
print("Your net income is:" , net_income)

