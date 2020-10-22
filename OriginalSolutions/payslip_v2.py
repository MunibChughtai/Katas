import csv

def main():
    print('Welcome to the payslip generator!')

    employee ={}
    employee_list= {   }
    #employee_list['Munib']['name'] = 'Munib'
    excel_inp='N'
    excel_inp = input('Do you want to use excel as input - (Y/N): ')

    if excel_inp == 'Y' or excel_inp=='y':
        with open('sal_input.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    # values saved using csv
                    employee['name'] = row[0]
                    employee['surname'] = row[1]
                    employee['annual_salary'] = int(row[2])
                    employee['super_rate'] = int(row[3].replace('%',''))
                    employee['payment_date'] = row[4]
                    # calculated values
                    employee['gross_income'] = find_gross_income(employee["annual_salary"])  # rounded
                    employee['income_tax'] = find_income_tax(employee["annual_salary"])  # rounded
                    employee['net_income'] = employee['gross_income'] - employee['income_tax']
                    employee['super'] = round(employee['gross_income'] * (employee['super_rate'] / 100))  # rounded

                    employee_list[employee['name']+employee['surname']] = employee
                    employee = {}
                    line_count += 1
            print(f'Input: {line_count-1} lines processed')
            #print(employee_list['DavidRudd']['name'])
            #print(employee_list['RyanChen']['name'])
            #print(employee_list)

            with open('sal_output.csv', mode='w') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                ctr=0
                for i in employee_list.values():
                    if ctr==0:
                        employee_writer.writerow(['Name', 'Surname', 'Annual Salary', 'Super Rate', 'Payment Date', 'Gross Income', 'Income Tax', 'Net Income', 'Super'])
                    employee_writer.writerow([i['name'], i['surname'], i['annual_salary'], str(i['super_rate'])+'%', i['payment_date'], i['gross_income'], i['income_tax'], i['net_income'], i['super'] ])
                    ctr+=1
                print(f'{ctr} rows written')
    else:
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