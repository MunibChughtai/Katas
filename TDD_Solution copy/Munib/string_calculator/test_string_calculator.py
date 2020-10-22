import pytest

from string_calculator import *

def test_input_str_ret_number():
    assert string_calculator('') == 0

def test1_single_no_input():
    assert string_calculator('1') == 1

def test2_single_no_input():
    assert string_calculator('3') == 3

def test3_single_no_input():
    assert string_calculator('100') == 100

def test1_two_number_input():
    assert string_calculator('1, 2') == 3

def test2_two_number_input():
    assert string_calculator('3, 5') == 8

def test1_any_number_input():
    assert string_calculator('1, 2, 3') == 6

def test2_any_number_input():
    assert string_calculator('3, 5, 3, 9') == 20

def test1_line_break_comma():
    assert string_calculator('1, 2\n 3') == 6

def test2_line_break_comma():
    assert string_calculator('3\n 5\n 3, 9') == 20

def test1_different_delimiters():
    assert string_calculator('//;\n1;2') == 3

def test2_different_delimiters():
    assert string_calculator('//;-\n1;2-3') == 6

def test2_different_delimiters(): # step 7
    with pytest.raises(ValueError) as e:
      string_calculator('-1, 2, -3')
    assert str(e.value) == 'Negatives not allowed: -1,-3'

def test_greater_1000():
    assert string_calculator('1000, 1001, 2') == 2

def test_multilength_delimeter():
    assert string_calculator('//[===]\n1===2===3') == 6 # tested for = and @, * gives error
    assert string_calculator('//[***]\n1***2***3') == 6

def test_multiple_delimeters():
    assert string_calculator('//[=][@]\n1=2@3') == 6
    assert string_calculator('//[*][%]\n1*2%3') == 6

def test_multiple_multicharacter_delimeters():
    assert string_calculator('//[===][@@][%]\n1===2@@3%4') == 10
    assert string_calculator('//[***][#][%]\n1***2#3%4') == 10

def test_multiple_multicharacter_delimeters():
    assert string_calculator('//[=1=][%]\n1=1=2%3') == 6
    assert string_calculator('//[*1*][%]\n1*1*2%3') == 6

#s = ''.join(re.split('\\[', '[@@@][***][===]')).replace(']', '|')
#s[:-1]
#delimiter_used = delimiter_used[0:-1]