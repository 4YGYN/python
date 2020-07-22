"""Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция должна
вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала
числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24."""

import math
from itertools import count


def fact(n):
    n = int(n)
    for el in count(n):
        yield math.factorial(el)


g = fact(input('Введите числовое значение: '))

x = 0
for el in g:
    if x < 6:
        print(el)
        x += 1
    else:
        break
