# -*- coding: utf-8 -*-

# Meno: Sičáková, Júlia
# Spolupráca: 
# Použité zdroje: prednaska, stackoverflow, geeksforgeeks
# Čas: asi hodina

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework7.md


class ClassA:
    def __init__(self, value):
        self.value = value

    def foo(self):
        return self.value

    def bar(self):
        return "something"


# TODO: upravte definíciu tak, aby ClassB bola podtriedou ClassA
class ClassB(ClassA):
    def __init__(self, value):
        # TODO: pridajte volanie konštruktora nadtriedy
        super().__init__(value)
        self.value = value/2
        obj = ClassA(testA)
        obj.foo()
        obj.bar()
    # TODO: prepíšte metódu foo tak, aby vrátila polovicu
    # návratovej hodnoty implementácie z nadtriedy
    # implementácia nech obsahuje volanie metódy foo z nadtriedy


test_value = 512
testA = ClassA(test_value)
testB = ClassB(test_value)

# TODO: do komentárov napíšte, z ktorej triedy sa vykonajú implementácie metód
print(testA.foo())  # implementácia z triedy Class A
print(testA.bar())  # implementácia z triedy Class A
print(testB.foo())  # implementácia z triedy Class B
print(testB.bar())  # implementácia z triedy Class B
