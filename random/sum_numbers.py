# -*- coding: utf-8 -*-
"""
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)

sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18

---solutions---
started: 
finished solutions at:
finished best implementation at:

#solution 1
    sumary: for every character in the string, if it is a number
    append it to the num string, otherwise, add it to the sum
    and clear the num string
"""

def sum_numbers(string):
    
    _sum = 0
    num = ""
    
    for s in string:
        if s.isdigit():
            num += s
        else:
            if num:
                _sum += int(num)
                num = ""

    if num:
        _sum += int(num)

    return _sum

assert sum_numbers("abc123xyz") == 123
assert sum_numbers("aa11b33") == 44
assert sum_numbers("7 11") == 18
