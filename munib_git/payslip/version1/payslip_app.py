import calendar
import csv

class payslip:
    def __init__(self): # this got introduced at getFullName stage
        self.reset_employee()
        self._employee_list = {}

    # ------------------------------------Getter and Setter----------------------------------------#
    #def consoleInput(self):
    #    self._annual_sal=0

    def setAnnualSal(self, p_ann_sal):
        if p_ann_sal <=0:
            raise Exception('Error* Non Positive Annual Salary.')
        else:
            self._employee['annual_sal'] = p_ann_sal
            self.setGrossIncome()
            self.setIncomeTax()
            self.set_netIncome()

    def getAnnualSal(self, d=-1):
        if d==-1:
            res = self._employee['annual_sal']
        else:
            res = self._employee_list[d]['annual_sal']
        return res

    def setSuperRate(self, superRate):
        if superRate <0 or superRate>50:
            raise Exception('Error* Super Rate cannot must be between 0 and 50 inclusive.')
        self._employee['superRate'] = str(superRate)+'%'
        self.setSuper()

    def getSuperRate(self, d=-1):
        if d==-1:
            res = int(self._employee['superRate'].replace('%',''))
        else:
            res = self._employee_list[d]['superRate']
        return res

    def setSuper(self): # this must be done after setting annual sal
        if self.getAnnualSal() >0:
            self._employee['super'] = round(self.getGrossIncome()* (self.getSuperRate()/100))

    def getSuper(self, d=-1):
        if d==-1:
            res = self._employee['super']
        else:
            res = self._employee_list[d]['super']
        return res

    def setDateRange(self, p_range):
        self._employee['date_range'] =p_range

    def getDateRange(self, d=-1):
        if d==-1:
            res = self._employee['date_range']
        else:
            res = self._employee_list[d]['date_range']
        return res

    def setFName(self, fname):
        self._employee['fName'] = fname

    def setLName(self, lname):
        self._employee['lName'] = lname

    def getFName(self, d = -1):
        if d==-1:
            res = self._employee['fName']
        else:
            res = self._employee_list[d]['fName']
        return res

    def getLName(self, d = -1):
        if d==-1:
            res = self._employee['lName']
        else:
            res = self._employee_list[d]['lName']
        return res

    def getFullName(self, d=-1):
        if self.getFName(d) =='' or self.getLName(d)=='':
            raise Exception('First or Last Name cannot be null')
        return f'{self.getFName(d)} {self.getLName(d)}'

    def setGrossIncome(self):
        self._employee['gross_income'] = round(self._employee['annual_sal']/12)

    def setIncomeTax(self):
        if self.getAnnualSal() <= 18200:
            self._employee['income_tax']=0
        elif self.getAnnualSal() >= 18201 and self.getAnnualSal() <= 37000:
            self._employee['income_tax']= round(((19/100) * (self.getAnnualSal() - 18200))/12)
        elif self.getAnnualSal() >= 37001 and self.getAnnualSal()<= 87000:
            self._employee['income_tax'] = round((3572 + ((32.5 / 100) * (self.getAnnualSal() - 37000)))/12)
        elif self.getAnnualSal() >= 87001 and self.getAnnualSal()<= 180000:
            self._employee['income_tax'] = round((19822 + ((37 / 100) * (self.getAnnualSal() - 87000))) / 12)
        elif self.getAnnualSal() >= 180001:
            self._employee['income_tax'] = round((54232 + ((45 / 100) * (self.getAnnualSal() - 180000))) / 12)
        else:
            self._employee['income_tax'] = -1

#--------------------------------------------------------------------------------------------------#
    def set_netIncome(self):
        self._employee['net_income'] = self.getGrossIncome() - self.getIncomeTax()

    def get_netIncome(self, d=-1):
        if d==-1:
            res = self._employee['net_income']
        else:
            res = self._employee_list[d]['net_income']
        return res

    def getGrossIncome(self, d=-1):
        if d==-1:
            res = self._employee['gross_income']
        else:
            res = self._employee_list[d]['gross_income']
        return res

    def getIncomeTax(self, d=-1):
        if d==-1:
            res = self._employee['income_tax']
        else:
            res = self._employee_list[d]['income_tax']
        return res

    def addEmployeeToDict(self):
        self._employee_list[self._employee['fName']+self._employee['lName']] = self._employee

    def setError(self, e_msg):
        self._employee['err'] += e_msg

    def getError(self, d=-1):
        if d==-1:
            res = self._employee['err']
        else:
            res = self._employee_list[d]['err']
        return res

    def reset_employee(self):
        self._employee = {'annual_sal': 0,
                          'superRate': 0,
                          'date_range': '',
                          'fName': '',
                          'lName': '',
                          'gross_income': 0,
                          'income_tax': 0,
                          'net_income': 0,
                          'super': 0,
                          'err':''
                          }
#--------- Though the records within empl dict are added into emp dict and checked via test cases, adding via file, not sure how to do it-----#
    def reading_csv_file(self):
        with open('sal_input.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.reset_employee()
                    self.setFName(row[0])
                    self.setLName(row[1])
                    try:
                        self.setAnnualSal(int(row[2]))
                    except Exception as e:
                        self.setError(str(e))
                    try:
                        self.setSuperRate(int(row[3].replace('%', '')))
                    except Exception as e:
                        self.setError(' '+str(e))

                    self.setDateRange(row[4])
                    self.addEmployeeToDict()
                    line_count += 1
            print(f'Input: {line_count - 1} lines processed')

# -------------------------------------- Writing to CSV (made without test cases)-----------------------------------------------#
    def writing_csv_file(self):
        with open('sal_output.csv', mode='w') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            ctr = 0
            for i in self._employee_list.values():
                if ctr == 0:
                    employee_writer.writerow(['Name', 'Surname', 'Annual Salary', 'Super Rate', 'Payment Date', 'Gross Income', 'Income Tax',
                                             'Net Income', 'Super', 'Message'])
                employee_writer.writerow([  self.getFName(i['fName']+ i['lName']),
                                            self.getLName(i['fName']+ i['lName']),
                                            self.getAnnualSal(i['fName']+ i['lName']),
                                            self.getSuperRate(i['fName']+ i['lName']),
                                            self.getDateRange(i['fName']+ i['lName']),
                                            self.getGrossIncome(i['fName']+ i['lName']),
                                            self.getIncomeTax(i['fName']+ i['lName']),
                                            self.get_netIncome(i['fName']+ i['lName']),
                                            self.getSuper(i['fName']+ i['lName']),
                                            self.getError(i['fName']+ i['lName'])
                                          ])
                ctr += 1
            print(f'{ctr} rows written')

#-------------------------------------- User Input (made without test cases)-----------------------------------------------#
    def console_input(self):
        err=0

        self.setFName(input('Please input your Name: '))
        self.setLName(input('Please input your Surname: '))
        try:
            self.setAnnualSal( int(input('Please input your Annual Salary: ')))
        except Exception as e:
            print(e)
            err= -1

        try:
            self.setSuperRate(int(input('Please input your Super Rate: ')))
        except Exception as e:
            print(e)
            err = -1

        self.setDateRange(input('Please enter your payment start and end date (DD Month): '))
        return err
#-------------------------------------- Console Output (made without test cases)-----------------------------------------------#
    def console_output(self, err):
        #if err == -1:
        print('\nYour Payslip has been generated with errors: \n' if err==-1 else '\nYour Payslip has been generated:')
        print(f'Full Name: {self.getFullName()}')
        print(f'Pay Period: {self.getDateRange()}')
        print(f'Gross Income: {self.getGrossIncome()}')
        print(f'Income Tax: {self.getIncomeTax()}')
        print(f'Net Income: {self.get_netIncome()}')
        print(f'Super: {self.getSuper()}')
        print(f'\nThank you for using MYOB!')
#-------------------------------------(made without test cases)----------------------------------------#
    def console_options(self):
        option=input('Do you want to use Excel to upload records (Y/N): ')
        if option == 'Y' or option =='y':
            self.reading_csv_file()
            self.writing_csv_file()
        else:
            err = self.console_input()
            self.console_output(err)
#-------------------------------------(made without test cases)----------------------------------------#
def main():
    ps = payslip()
    ps.console_options()

if __name__ == '__main__':
    main()