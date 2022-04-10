# -*- coding: utf-8 -*-

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework5.md

# skvelé riešenie - 2b

# 9
def decimal_to_binary(number):
    # converts a decimal positive integer to binary
    # input should be a positive integer
    string = ""
    while (number // 2 != 0):
        string = str(number % 2) + string
        number = number // 2
    string = "1" + string
    return string

def test_decimal_to_binary():
    
    assert decimal_to_binary(-4) == False
    assert decimal_to_binary(0) == False
    assert decimal_to_binary(-1) == False
    
    print("Test for invalid input")
   
    assert decimal_to_binary(23) == "10111"
    assert decimal_to_binary(17) == "10001"
    assert decimal_to_binary(89) == "1011001"
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(9) == "1001"
    assert decimal_to_binary(46) == "101110"
    assert decimal_to_binary(67) == "100011"
    assert decimal_to_binary(14) == "1110"
    assert decimal_to_binary(28) == "11100"
    assert decimal_to_binary(72) == "1001000"
    assert decimal_to_binary(90) == "1011010"
    
    
    print("All tests passed")
    
    pass

if __name__ == '__main__':
    test_decimal_to_binary()
