# -*- coding: utf-8 -*-

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

    def foo(self):
        ClassA.foo(self)
        return self.value * 2

    # TODO: prepíšte metódu foo tak, aby vrátila dvojnásobok
    # návratovej hodnoty implementácie z nadtriedy
    # implementácia nech obsahuje volanie metódy foo z nadtriedy


test_value = 2
testA = ClassA(test_value)
testB = ClassB(test_value)

# TODO: do komentárov napíšte, z ktorej triedy sa vykonajú implementácie metód
print(testA.foo())  # implementácia z triedy ClassA
print(testA.bar())  # implementácia z triedy ClassA
print(testB.foo())  # implementácia z triedy ClassB
print(testB.bar())  # implementácia z triedy ClassA
