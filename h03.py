# -*- coding: utf-8 -*-

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework3.md

import random
import string

import numpy
import pandas

# --------------------
# Úloha 1
# Načítajte dataset uložený v súbore h03.csv ako pandas DataFrame
# a určte pomocou metód pandas dataframe (alebo cez použitie numpy poľa):
#  - váhu najmladšieho muža

import pandas as pd 

df = pd.read_csv(r'C:\Users\allwa\Untitled Folder\h03.csv')


df = df[df['gender']=='M']
df.sort_values(by=['age'], inplace=True, ascending=True)

print(df['weight'].head(1).to_csv(index=False))


# --------------------
# Úloha 2
# V kóde nižšie sa vygeneruje dvojrozmerné numpy pole s náhodnými číselnými
# hodnotami. Vypočítajte:
#  - maximálnu hodnotu po riadkoch
#array = numpy.random.rand(5, 5)
#print(array)

import numpy as np
array = np.random.rand(5, 5)
print(array)

print(np.max(array, axis=1))

# --------------------
# Úloha 3

# 6. Máme zoznam čísel lst. Pomocou list comprehension vygenerujte zoznam lst2,
# ktorý bude obsahovať iba tie prvky zoznamu lst, ktoré po celočíselnom delení
# piatimi dajú nepárny zvyšok.
import random
lst = [random.randint(1, 1000) for _ in range(20)]
print(lst)
lst2 = [num for num in lst if num % 5 == 1 or num % 5 == 3]
print(lst2)


# 10. Máme zoznam čísel lst. Pomocou list comprehension vygenerujte zoznam lst2,
# ktorý bude obsahovať iba dvojciferné párne prvky zoznamu lst.
import random
lst = [random.randint(1, 1000) for _ in range(20)]
print(lst)
lst2 = [num for num in lst if num / 10 >= 1 and num / 10 <= 9.9 and num % 2 == 0]
print(lst2)
