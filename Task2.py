"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

el = int(input('Введите количество элеметов списка: '))
list_ = []
i = 0
e = 0
while i < el:
    list_.append(input('Введите значение спика: '))
    i += 1

for elem in range(int(len(list_) / 2)):
    list_[e], list_[e + 1] = list_[e + 1], list_[e]
    e += 2
print(list_)
