start = int(input("Сколько килметров пробежал спорсмен в первый день: "))
rez = int(input("Сколько минимум километров хочет пробегать спорстмен: "))

day = 1
if start == rez:
    print(f'Достигнете результата в {day} день')
else:
    while rez >= start:
        day += 1
        start = ((start * 0.1) + start)
    print(f"Достигнете результат на {day} день")