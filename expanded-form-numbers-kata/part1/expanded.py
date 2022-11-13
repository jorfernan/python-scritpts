#!/usr/bin/env python3
"""Takes an input integer and returns its expanded form"""
def expanded_form(num):
    # Created an empty string to return
    res = ""
    # Turning input integer into a string
    string_num = str(num)
    # Storing the lenght of the previously casted string
    figures = len(string_num)

    # Looping through the string
    for digit in string_num:
        # If the current digit is 0, reduces by one the current figure and continues
        if digit  == "0":
            figures -= 1
            continue
        # Reduces the amount of zeros that follow the digit
        # Adds the current digit followed by the amount of zeros that are needed to the res variable
        figures-=1
        res += digit + "0"*figures + " + "
    # Deletes the " +" extra with [:-2] from the string and the blank spaces with strip()
    return res[:-2].strip()