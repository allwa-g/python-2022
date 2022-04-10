# -*- coding: utf-8 -*-

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework4.md


# 17
def get_sum_of_multiples(max_number, number):
    # returns the sum of all multiples of number in interval [1, maxNumber]
    # both inputs should be positive integers

    # TODO: check the validity of inputs, correct error in code
    # e.g. what if max_number and number are not positive integers?
    
    if max_number < 1 or number < 0:
        raise ValueError("Input value must be an integer bigger than 0.")    
    if number == 0:
        raise ZeroDivisionError("You're trying to divide by zero.")
    if type(max_number) != int:
        raise TypeError("Input value of max number must be an integer.")
    if type(number) != int:
        raise TypeError("Input value of number must be an integer.")

    sum_of_multiples = 0
  
    for num in range(max_number + 1):
        if num % number == 0:
            sum_of_multiples += num
    return sum_of_multiples
print(get_sum_of_multiples(10,8))
