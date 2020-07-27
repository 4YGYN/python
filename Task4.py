
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

"""
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4_1.txt', 'a', encoding='utf-8')  as new_file:
    with open('text_4.txt', encoding='utf-8') as my_file:
        line = my_file.read().split('\n')
        for i in line:
            i = i.split(' - ')
            new_file.writelines(rus[i[0]] + ' - ' + i[1] + '\n')
