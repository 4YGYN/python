"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 2 or month == 12:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif 3 <= month <= 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif 6 <= month <= 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif 9 <= month <= 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print('На земле только 12 месяцев')