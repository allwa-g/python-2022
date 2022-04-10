# -*- coding: utf-8 -*-

# Meno: Sičáková, Júlia
# Spolupráca: 
# Použité zdroje: prednasky
# Čas: 30 minut

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework6.md

# TODO: add your definition of the class

class SpanielDog:
    
    breed = str(None)

    def __init__(self, name:str, age:int):
        self.name = name
        self.__age = age
        
#     def get_breed(self):
#         return self.breed  
    
#     def get_age(self): 
#         return self._age
    

    def get_age():
        return int(SpanielDog.__age)
    
    
    def __str__(self):
        return "SpanielDog: {} {}".format(
            str(self.name), str(self.__age))

    
# x = SpanielDog("Buddie", 5)
# print(x)
    
    