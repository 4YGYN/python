'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры
'''

Name = input('Введите ваше имя: ')
Surname = input('Введите вашу фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Ваш email: ')
pnum = input('Номер вашего телефона: ')

def fam():
    return (f'имя - {Name}, фамилия - {Surname}, год рождения - {year}, город проживания - {city}, email - {email}, номер телефона - {pnum}')

print(f'Ваши данные: {fam()}')

""" Понимаю, что через списки или ключи сделать проще, но я пока не разобрался  в них"""