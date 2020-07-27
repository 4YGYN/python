"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

sum_el = 0

with open('Test5.txt', 'w+', encoding='utf=8') as t5:
       for i in range (10):
                el = randint(1, 100)
                sum_el += el
                t5.write(str(el) + ' ')

print(f'Сумма - {sum_el}')

