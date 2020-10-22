import pytest

from payslip_app import Payslip

@pytest.fixture()
def john_instance():
    return Payslip('John', 'Doe', 60050, 9, '1 March', '31 March')

@pytest.fixture()
def ahmed_instance():
    return Payslip('Ahmed', 'Shehzad', 120000, 10, '1 March', '31 March')

def test_name_t1(john_instance):
    assert john_instance.get_name() == 'John Doe'

def test_pay_period_t1(john_instance):
    assert john_instance.get_pay_period() == '1 March - 31 March'

def test_gross_income_t1(john_instance):
    assert john_instance.get_gross_income() == 5004

def test_income_tax_t1(john_instance):
    assert john_instance.get_income_tax() == 922

def test_net_income_t1(john_instance):
    assert john_instance.get_net_income() == 4082

def test_super_t1(john_instance):
    assert john_instance.get_super() == 450

#-------------


def test_name_t2(ahmed_instance):
    assert ahmed_instance.get_name() == 'Ahmed Shehzad'

def test_pay_period_t2(ahmed_instance):
    assert ahmed_instance.get_pay_period() == '1 March - 31 March'

def test_gross_income_t2(ahmed_instance):
    assert ahmed_instance.get_gross_income() == 10000

def test_income_tax_t2(ahmed_instance):
    assert ahmed_instance.get_income_tax() == 2669

def test_net_income_t2(ahmed_instance):
    assert ahmed_instance.get_net_income() == 7331

def test_super_t2(ahmed_instance):
    assert ahmed_instance.get_super() == 1000