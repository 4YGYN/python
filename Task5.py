def my_sum ():
    sum_res = 0
    while True:
        number = input('Введите числа через пробел или "q" для выхода - ').split()
        for el in number:
            if el == 'q' or el == 'Q':
                print(f'Конец работы программы. Филинальная сумма - {sum_res}')
                return sum_res
            else:
                try:
                    sum_res =+ int(el)
                except ValueError:
                    print("Введите числа через пробел или 'q' для выхода - ")
        print(f'Финальная сумма - {sum_res}')


my_sum()