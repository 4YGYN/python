pribil = int(input('Укажите вашу прибыль: '))
rashodi = int(input('Укажите ваше расходы: '))

raznica = pribil - rashodi

if raznica < 0 :
    print(f'Увы, вы заработали меньше чем потратили.\nРасходы больше доходов на {raznica} рублей.')
elif raznica >=0 :
    print(f'Ваша прибыль {raznica} рублей')
    rent = (raznica / pribil) * 100
    print(f"Ваша рентабильность {rent:.2f} %")
    people = int(input('Какое колличество сотрудников у Вас работает: '))
    rent_p = pribil / people
    print(f"Прибыль фирмы с расчетом на одного сотрудника составляет {rent_p:.2f} рублей")
