import re

def string_calculator(input_string):
    if input_string=='':
        return 0

    #if input_string.find(',')==-1 and input_string.find('\n')==-1 and input_string.find('//')==-1:
    #    return int(input_string)

    #if len(input_string)==1:
    #    return int(input_string)

    if input_string[0:2] != '//':
        split_input = re.split(',|\n', input_string)
    else:
       delimiter_used =''

       for j in input_string[2 : input_string.find('\n')]: # [**] [++] [^^]
           if input_string[2] != '[':
               delimiter_used = delimiter_used + j +'|'
           else:
               if j =='[':
                   continue
               elif j == ']':
                   delimiter_used +=  '|'
               elif j.isalnum():
                   delimiter_used += j
               else:
                   delimiter_used += '\\' + j

       delimiter_used = delimiter_used[0:-1]

       split_input = re.split(delimiter_used, input_string[input_string.find('\n')+1:])

    sum = 0
    negative_nos_str = ''

    for i in split_input:
        if int(i) < 0:
            negative_nos_str += str(int(i))+','

        if negative_nos_str != '' or int(i)>=1000:
            continue
        sum += int(i)

    if negative_nos_str == '':
        return sum
    else:
        raise ValueError(f'Negatives not allowed: {negative_nos_str[0:-1]}')