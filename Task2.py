"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


"""with open("T2.txt", "r", encoding="utf-8") as task2:
    f = task2.read()
    print(f'Содержимое файла:\n {f}')
    f = task2.readlines()
    print(f"Количество строк - {len(f)}")
    f = task2.read()
    f = f.split()
    print(f'{len(f)}')"""

my_file = open('T2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('T2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('T2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

#Не понимаю почему верхнее так не работает (что в комментариях)