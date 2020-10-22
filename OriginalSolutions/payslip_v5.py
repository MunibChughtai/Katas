import csv

def main():
    print('Welcome to the payslip generator!')

    employee ={}
    employee_list= {}
    err=''

    excel_inp='N'
    excel_inp = input('Do you want to use excel as input - (Y/N): ')

    if excel_inp == 'Y' or excel_inp=='y':
        excel_io(employee, employee_list)

    else:
        console_input(employee)
        print('\n\nThank you for using MYOB!')

def annual_sal_chk(annual_sal):
    global err
    annual_sal_flag=0
    if annual_sal <= 0:
        err= 'Annual Sal must not be less than or equal to 0.'
        annual_sal_flag=-1
    return annual_sal_flag

def chk_super(super_rate):
    global err
    super_flag=0
    if super_rate <= 0 or super_rate > 100:
        super_flag=-1
        err += ' Super value must be within (1-100)%.'
    return super_flag

def chk_date_name(name, surname, payment_date):
    global err
    date_name_flag=0
    if payment_date=='':
        err+=' Payment date cannot be null.'
        date_name_flag=-1
    if name =='':
        err += ' Name cannot be null.'
        date_name_flag = -1
    if surname =='':
        err += ' Surname cannot be null.'
        date_name_flag = -1
    return date_name_flag

def excel_io(employee, employee_list):
    global err

    with open('sal_input.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                err=''
                annual_sal_flag=0
                super_flag=0
                date_name_flag=0

                # values saved using csv
                employee['name'] = row[0]
                employee['surname'] = row[1]
                employee['annual_salary'] = int(row[2])
                annual_sal_flag = annual_sal_chk(employee['annual_salary'])

                employee['super_rate'] = int(row[3].replace('%', ''))
                super_flag = chk_super(employee['super_rate'])

                employee['payment_date'] = row[4]
                date_name_flag = chk_date_name(employee['name'], employee['surname'], employee['payment_date'])

                if date_name_flag ==0:
                    # calculated values
                    if annual_sal_flag==0:
                        employee['gross_income'] = find_gross_income(employee["annual_salary"])  # rounded
                        employee['income_tax'] = find_income_tax(employee["annual_salary"])  # rounded
                        employee['net_income'] = employee['gross_income'] - employee['income_tax']
                        if super_flag==0:
                            employee['super'] = round(employee['gross_income'] * (employee['super_rate'] / 100))  # rounded
                        else:
                            employee['super'] = 'NA'
                    else:
                        employee['gross_income']='NA'
                        employee['income_tax']='NA'
                        employee['net_income']='NA'
                        employee['super']='NA'
                else:
                    if employee['name'] == '':
                        employee['name']='Error'
                    else:
                        employee['name'] = employee['name']

                    if employee['surname'] =='':
                        employee['surname']='Error'
                    else:
                        employee['surname'] = employee['surname']

                    if employee['payment_date']=='':
                        employee['payment_date']='Error'
                    else:
                        employee['payment_date'] = employee['payment_date']

                    employee['gross_income'] = 'NA'
                    employee['income_tax'] = 'NA'
                    employee['net_income'] = 'NA'
                    employee['super'] = 'NA'

                employee['message'] = err
                employee_list[employee['name'] + employee['surname']] = employee
                employee = {}
                line_count += 1

        print(f'Input: {line_count - 1} lines processed')

        with open('sal_output.csv', mode='w') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            ctr = 0
            for i in employee_list.values():
                if ctr == 0:
                    employee_writer.writerow(
                        ['Name', 'Surname', 'Annual Salary', 'Super Rate', 'Payment Date', 'Gross Income', 'Income Tax',
                         'Net Income', 'Super', 'Message'])
                employee_writer.writerow(
                    [i['name'], i['surname'], i['annual_salary'], str(i['super_rate']) + '%', i['payment_date'],
                     i['gross_income'], i['income_tax'], i['net_income'], i['super'], i['message']])
                ctr += 1
            print(f'{ctr} rows written')


def console_input(employee):
    employee['name'] = input('Please input your name: ')
    employee['surname'] = input('Please input your surname: ')
    employee['annual_salary'] = int(input('Please enter your annual salary: '))
    employee['super_rate'] = int(input('Please enter your super rate: '))
    employee['payment_start_date'] = input('Please enter your payment start date: ')
    employee['payment_end_date'] = input('Please enter your payment end date: ')

    print('\n\nYou payslip has been generated:\n')

    employee['gross_income'] = find_gross_income(employee["annual_salary"])  # rounded
    employee['income_tax'] = find_income_tax(employee["annual_salary"])  # rounded
    employee['net_income'] = employee['gross_income'] - employee['income_tax']
    employee['super'] = round(employee['gross_income'] * (employee['super_rate'] / 100))  # rounded

    print(f'Name: {employee["name"]} {employee["surname"]}')
    print(f'Pay Period {employee["payment_start_date"]} - {employee["payment_end_date"]}')
    print(f'Gross Income: {employee["gross_income"]}')
    print(f'Income Tax: {employee["income_tax"]}')
    print(f'Net Income: {employee["net_income"]}')
    print(f'Super: {employee["super"]}')

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