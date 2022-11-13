#!/usr/bin/env python3
from re import search
def expanded_form(num):
    
    res = ""

    pattern = "(.*)\.(.*)"
    division = search(pattern,str(num))

    integer_part,decimal_part = division.group(1),division.group(2)
    integer_part_len = len(integer_part)
    
    for digit in integer_part:
        if digit == "0":
            integer_part_len -= 1
            continue
        integer_part_len -=1
        res += digit + "0"*integer_part_len + " + "
    
    decimal_cont = 1
    for digit in decimal_part:
        if digit == "0":
            decimal_cont +=1
            continue
        res += digit+"/1"+"0"*decimal_cont + " + "
        decimal_cont+=1
    
    return res[:-2].strip()



expanded_form(7304.304)
