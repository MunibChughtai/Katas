import calendar

class payslip:
    def __init__(self): # this got introduced at getFullName stage
        self._employee = {'annual_sal':0,
                          'superRate':0,
                          'date_range':'',
                          'fName':'',
                          'lName':'',
                          'gross_income':0,
                          'income_tax':-1,
                          'net_income':0,
                          'super':0
                          }

    # ------------------------------------Getter and Setter----------------------------------------#
    #def consoleInput(self):
    #    self._annual_sal=0

    def setAnnualSal(self, p_ann_sal):
        if p_ann_sal <=0:
            raise Exception('Non Positive Annual Salary')
        else:
            self._employee['annual_sal'] = p_ann_sal
            self.setGrossIncome()
            self.setIncomeTax()
            self.set_netIncome()

    def getAnnualSal(self):
        return self._employee['annual_sal']

    def setSuperRate(self, superRate):
        if superRate <0 or superRate>50:
            raise Exception('Super Rate cannot must be between 0 and 50 inclusive')
        self._employee['superRate'] = superRate
        self.setSuper()

    def getSuperRate(self):
        return self._employee['superRate']

    def setSuper(self): # this must be done after setting annual sal
        if self.getAnnualSal() >0:
            self._employee['super'] = round(self.getGrossIncome()* (self.getSuperRate()/100))

    def getSuper(self):
        return self._employee['super']

    def setDateRange(self, p_month, p_year):
        end_date = calendar.monthrange(p_year,p_month)[1]
        self._employee['date_range'] =f'1-{p_month}-{p_year} till {end_date}-{p_month}-{p_year}'

    def getDateRange(self):
        return self._employee['date_range']

    def setFName(self, fname):
        self._employee['fName'] = fname

    def setLName(self, lname):
        self._employee['lName'] = lname

    def getFName(self):
        return self._employee['fName']

    def getLName(self):
        return self._employee['lName']

    def getFullName(self):
        if self.getFName() =='' or self.getLName()=='':
            raise Exception('First or Last Name cannot be null')
        return f'{self.getFName()} {self.getLName()}'

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

    def get_netIncome(self):
        return self._employee['net_income']

    def getGrossIncome(self):
        return self._employee['gross_income']

    def getIncomeTax(self):
        return self._employee['income_tax']
