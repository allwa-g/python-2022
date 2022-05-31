# -*- coding: utf-8 -*-
# Spolupráca:
# Použité zdroje:
# Čas:

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework2.md


# 14. Napíšte funkciu, ktorá má jeden parameter - kladné celé číslo n
# a vráti sumu (ako integer) všetkých násobkov čísla 3 a 5 menšie ako n.

def multiples(x):
    n = 0
    summary = 0
    for i in range(1, x):
        if i % 5 == 0 and i % 3 == 0:
            summary += i
    return summary


multiples(45)

# --------------------


# 39. Máme zoznam náhodných reťazcov lst. Upravte zoznam pomocou
# lambda výrazu tak, že všetky reťazce otočíte.
# lst = [''.join(random.choices(string.ascii_lowercase, k=6)) for _ in range(20)]
# print(lst)
# edited_list = list(map( k -1, lst))
# print(edited_list)

import random
import string

lst = [''.join(random.choices(string.ascii_lowercase, k=6)) for _ in range(20)]
print(lst)
edited_list = list(map(lambda k: "".join(reversed(k)), lst))
print(edited_list)


# --------------------

# 18. Zadefinujte generátor, ktorý postupne vygeneruje prvky číselného radu:
# s(k) = k ^ 3, kde k je poradové číslo prvku.


def generator(k):
    for i in range(1, k):
        n = pow(i, 3)
        yield n


gen = generator(6)
for _ in range(10):
    print(next(gen))
