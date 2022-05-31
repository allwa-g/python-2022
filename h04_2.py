# -*- coding: utf-8 -*-

# Meno: Sičáková, Júlia
# Spolupráca: 
# Použité zdroje: 
# Čas: 

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework4.md


# 27
def convert_to_float(number_str):
    # converts a string to a float, the string contains ',' we therefore
    # cannot use simple conversion
    # input should be a string representing a number with decimal comma

    # TODO: check the validity of input, amend optimistic code
    # e.g. is number_str a string? Does it contain ','?
    # Does it represent a decimal number?
    # Can we convert the two halves to integers, do they contain only numbers?
    
    if type(number_str) != str:
        raise TypeError("Invalid input - input should be string")
    if "," not in number_str:
        raise SyntaxError("Input should contain ,")

    whole, decimal = number_str.split(',')
    
    if (whole.isdecimal()) == False or (decimal.isdecimal() == False):
        raise TypeError("contains letters")
        
    if(whole != int) or (decimal != int):
        decimal_n = int(decimal)
        whole_n = int(whole)

    decimal_len = len(decimal)
    decimal_part = int(decimal) / (10 ** decimal_len)

    return float(whole) + decimal_part
#print(convert_to_float('34,5'))