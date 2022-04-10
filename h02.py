# -*- coding: utf-8 -*-

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework2.md


# 2. Napíšte funkciu, ktorá má jeden parameter - kladné celé číslo n
# a vráti zoznam všetkých násobkov čísla 3 a 4 menšie ako n.


def multiples(n):
    for x in range(1, n): 

        if x % 3 == 0 and x % 4 == 0: 

            print(x) 
            
multiples(89)


# --------------------


# 34. Máme zoznam trojciferných čísel lst. Vygenerujte zoznam pomocou lambda
# výrazu tak, aby prvky nového zoznamu boli prvé číslice pôvodného čísla
# na danej pozícii v zozname lst.
lst = [random.randint(100, 999) for _ in range(20)]
print(lst)
# edited_list = list(map( sem doplňte lambda výraz, lst))
# print(edited_list)


import random
import string

lst = [random.randint(100, 999) for _ in range(20)]
print(lst)
edited_list = list(map(lambda x: (x // 100) ,lst))
print(edited_list)
# --------------------

# 23. Zadefinujte generátor, ktorý postupne vygeneruje prvky číselného radu,
# kde ďalší prvok vypočítame nasledovne:
# - ak predošlý prvok bol nepárny, tak s(k + 1) = s(k) + 1;
# - ak predošlý prvok bol párny, tak s(k + 1) = s(k) / 2.
# Rad začnite ľubovoľným kladným celým číslom. Všetky prvky radu sú celé čísla.



def generator():
    a = 89
    while True:
        yield a
        if a % 2 == 0:
            a = a / 2
        elif a % 2 != 0:  # zbytočná podmienka, stačí else
            a = a + 1
gen = generator()
for _ in range(10):
    print(int(next(gen)))
