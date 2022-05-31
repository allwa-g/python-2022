# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework8.md

import random

import matplotlib.pyplot as plt
import numpy as np



def generate_numbers(n, interval):
    a, b = interval

    numbers = list()
    for _ in range(n):
        numbers.append(random.randint(a, b))

    return numbers


def plot_distribution(numbers):
    x = (numbers)

    plt.hist(x,n, align = 'left', width = 0.3)
    
    plt.xlabel("Vylosované číslo")
    plt.ylabel("Počet koľkokrát bolo číslo vylosované")
    plt.title("Početnosť jedinečných hodnôt v zozname náhodne generovaných hodnôt")
    plt.axhline(n/6, color='red')
    plt.margins(x = 0.15)

    plt.show()
    

if __name__ == '__main__':
    n = 10000
    interval = (1, 6)
    numbers = generate_numbers(n, interval)
    plot_distribution(numbers)
    #print(numbers)
    
