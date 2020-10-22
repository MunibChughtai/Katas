def main():
    print('Welcome to the payslip generator!')

    employee ={}

    employee['name'] = input('Please input your name: ')
    employee['surname'] = input('Please input your surname: ')
    employee['annual_salary'] = int(input('Please enter your annual salary: '))
    employee['super_rate'] = int(input('Please enter your super rate: '))
    employee['payment_start_date'] = input('Please enter your payment start date: ')
    employee['payment_end_date'] = input('Please enter your payment end date: ')

    print('\n\nYou payslip has been generated:\n')

    employee['gross_income'] = find_gross_income(employee["annual_salary"])  # rounded
    employee['income_tax'] = find_income_tax(employee["annual_salary"])     # rounded
    employee['net_income'] = employee['gross_income'] - employee['income_tax']
    employee['super'] = round(employee['gross_income'] * (employee['super_rate']/100)) # rounded

    print(f'Name: {employee["name"]} {employee["surname"]}')
    print(f'Pay Period {employee["payment_start_date"]} - {employee["payment_end_date"]}')
    print(f'Gross Income: {employee["gross_income"]}')
    print(f'Income Tax: {employee["income_tax"]}')
    print(f'Net Income: {employee["net_income"] }')
    print(f'Super: {employee["super"]}')
    print('\n\nThank you for using MYOB!')

def find_income_tax(annual_sal):
    annual_tax = 0

    if annual_sal <= 18200:
        annual_tax=0
    elif annual_sal >= 18201 and annual_sal <= 37000:
        annual_tax = (annual_sal - 18200) * (19/100)  # 19 Cents for each dollar above 18200
    elif annual_sal >= 37001 and annual_sal <= 87000:
        annual_tax = 3572 + ((annual_sal - 37000) * (32.5/100)) # 32.5 Cents for each dollar above 37000
    elif annual_sal >= 87001 and annual_sal <= 180000:
        annual_tax = 19822 + ( (annual_sal - 87000) * (37/100)  ) # 37 Cents for each dollar above 87000
    elif annual_sal >= 180001:
        annual_tax = 54232 + ((annual_sal - 180000) * (45 / 100)) # 45 Cents for each dollar above 180000

    monthly_tax = round(annual_tax/12)
    return monthly_tax

def find_gross_income(annual_sal):
    gross_income = round(annual_sal/12)
    return gross_income

if __name__ == "__main__":
    main()