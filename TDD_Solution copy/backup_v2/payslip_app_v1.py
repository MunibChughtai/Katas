import calendar

class payslip:
    def __init__(self): # this got introduced at getFullName stage
        #self._annual_sal =0
        #self._superRate=0
        #self._date_range=''
        #self._fName=''
        #self._lName=''
        self._employee = {'annual_sal':0,
                          'superRate':0,
                          'date_range':'',
                          'fName':'',
                          'lName':'',
                          'gross_income':0
                          }

    # ------------------------------------Getter and Setter----------------------------------------#
    #def consoleInput(self):
    #    self._annual_sal=0

    def setAnnualSal(self, p_ann_sal):
        if p_ann_sal <=0:
            raise Exception('Non Positive Annual Salary')
        else:
            #self._annual_sal = p_ann_sal
            self._employee['annual_sal'] = p_ann_sal
            self.setGrossIncome()

    def getAnnualSal(self):
        return self._employee['annual_sal']

    def setSuper(self, superRate):
        if superRate <0 or superRate>50:
            raise Exception('Super Rate cannot must be between 0 and 50 inclusive')
        #self._superRate = superRate
        self._employee['superRate'] = superRate

    def getSuper(self):
        return self._employee['superRate']

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
#--------------------------------------------------------------------------------------------------#

    def getGrossIncome(self):
        return self._employee['gross_income']
