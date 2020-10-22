import calendar
import csv

class Payslip:
    def __init__(self,
                 first_name,
                 last_name,
                 annual_salary,
                 super_rate,
                 payment_start_date,
                 payment_end_date
                 ):

        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.super_rate = super_rate
        self.payment_start_date = payment_start_date
        self.payment_end_date = payment_end_date

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_pay_period(self):
        return f'{self.payment_start_date} - {self.payment_end_date}'

    def get_gross_income(self):
        return round(self.annual_salary / 12)

    def get_income_tax(self):
        if self.annual_salary <= 18200:
            return 0
        elif  self.annual_salary >= 18201 and self.annual_salary <= 37000:
            return round( (  (19/100) * (self.annual_salary - 18200) ) /12   )
        elif self.annual_salary >= 37001 and self.annual_salary<= 87000:
            return round((3572 + ((32.5 / 100) * (self.annual_salary - 37000)))/12)
        elif self.annual_salary >= 87001 and self.annual_salary<= 180000:
            return round((19822 + ((37 / 100) * (self.annual_salary - 87000))) / 12)
        elif self.annual_salary >= 180001:
            return round((54232 + ((45 / 100) * (self.annual_salary - 180000))) / 12)

    def get_net_income(self):
        gross_income = self.get_gross_income()
        income_tax   = self.get_income_tax()
        res = gross_income - income_tax
        return res


    def get_super(self):
        return round(self.get_gross_income() * (self.super_rate / 100))


