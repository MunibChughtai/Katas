import re

def add_escape_character(input_str):
    res=''
    for i in input_str:
        if i.isalnum() or i=='|':
            res += i
        else:
            res += '\\'+i
    return res

def sum_list(split_input):
    sum = 0
    negative_nos_str = ''
    for i in split_input:
        if i=='':
            continue
        if int(i) < 0:
            negative_nos_str += str(int(i)) + ','
        if negative_nos_str != '' or int(i) >= 1000:
            continue
        sum += int(i)
    if negative_nos_str == '':
        return sum
    else:
        raise ValueError(f'Negatives not allowed: {negative_nos_str[0:-1]}')

def string_calculator(input_string):
    if input_string=='':
        return 0

    if input_string[0:2] != '//':
        split_input = re.split(',|\n', input_string)
    else:
       delimiter_used =input_string[2 : input_string.find('\n')]
       delimiter_used = delimiter_used.replace('[','').replace(']','|')
       delimiter_used = add_escape_character(delimiter_used)
       split_input = re.split(delimiter_used, input_string[input_string.find('\n')+1:])
    res = sum_list(split_input)
    return res

//[@@@][===]\n 1@@@2===3
[@@@][===]
\\@\\@\\@]|\\=\\=\\=|

[1, 2, 3]



