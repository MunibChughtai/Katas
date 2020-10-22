import pytest
from pytest import approx

from payslip_app import payslip

@pytest.fixture()
def classInitialized():
    ps = payslip()
    return ps


def test_positive_annualSal(classInitialized):
    #ps = payslip()
    classInitialized.setAnnualSal(200000)
    assert classInitialized.getAnnualSal() > 0

def test_nonPositive_annualSal(classInitialized):
    with pytest.raises(Exception):
        classInitialized.setAnnualSal(-50)

def test_superRatePositiveTest(classInitialized):
    classInitialized.setSuperRate(9)
    assert classInitialized.getSuperRate() >=0 and classInitialized.getSuperRate()<=50
    classInitialized.setSuperRate(0)
    assert classInitialized.getSuperRate() >= 0 and classInitialized.getSuperRate() <= 50
    classInitialized.setSuperRate(50)
    assert classInitialized.getSuperRate() >= 0 and classInitialized.getSuperRate() <= 50

def test_superRateNegativeTest(classInitialized):
    with pytest.raises(Exception):
        classInitialized.setSuperRate(-1)

    with pytest.raises(Exception):
        classInitialized.setSuperRate(51)

#def test_payment_date(classInitialized):
#    classInitialized.setDateRange(10, 2020)
#    assert classInitialized.getDateRange() == '1-10-2020 till 31-10-2020'

def test_input_name_saved(classInitialized):
    classInitialized.setFName('John')
    classInitialized.setLName('Doe')
    assert classInitialized.getFName() == 'John' and classInitialized.getLName()=='Doe'
    assert classInitialized.getFullName() == 'John Doe'

def test_input_name_not_null(classInitialized):
    with pytest.raises(Exception):
        classInitialized.setFName('Munib')
        classInitialized.getFullName()

def test_gross_income(classInitialized):
    classInitialized.setAnnualSal(60050)
    assert classInitialized.getGrossIncome() == 5004

def test_tax_value(classInitialized):
    classInitialized.setAnnualSal(18200)
    assert classInitialized.getIncomeTax()== 0

    classInitialized.setAnnualSal(30000)
    assert classInitialized.getIncomeTax() == 187

    classInitialized.setAnnualSal(37001)
    assert classInitialized.getIncomeTax() == 298

    classInitialized.setAnnualSal(60050)
    assert classInitialized.getIncomeTax() == 922

    classInitialized.setAnnualSal(90000)
    assert classInitialized.getIncomeTax() == 1744

    classInitialized.setAnnualSal(200000)
    assert classInitialized.getIncomeTax() == 5269

def test_net_income(classInitialized):
    classInitialized.setAnnualSal(60050)
    assert classInitialized.get_netIncome() == 4082

def test_getSuper(classInitialized):
    classInitialized.setAnnualSal(60050)
    classInitialized.setSuperRate(9)
    assert classInitialized.getSuper() == 450

def test_AddEmployeeDatatoDict(classInitialized):
    classInitialized.setFName('John')
    classInitialized.setLName('Doe')
    classInitialized.setAnnualSal(60050)
    classInitialized.setSuperRate(9)
    classInitialized.addEmployeeToDict()
    assert classInitialized.getFullName() == classInitialized.getFullName('JohnDoe')
    assert classInitialized.getAnnualSal() == classInitialized.getAnnualSal('JohnDoe')
    assert classInitialized.getGrossIncome() ==classInitialized.getGrossIncome('JohnDoe')
    assert classInitialized.getIncomeTax() == classInitialized.getIncomeTax('JohnDoe')
    assert classInitialized.get_netIncome() == classInitialized.get_netIncome('JohnDoe')
    assert classInitialized.getSuper() == classInitialized.getSuper()
    #assert 'Johny' == classInitialized.getFName('JohnDoe')