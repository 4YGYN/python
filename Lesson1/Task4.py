n = int(input('Введите любомое целое положительное число: '))

max = n % 10
number = n // 10

if max == 9:
    print('Максимальное чилсо: %d' % max)
else:
    while number > 0:
        if number % 10 > max:
            max = number % 10
        number = number // 10
    print('Максимальное чилсо: %d' % max)
