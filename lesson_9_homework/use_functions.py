"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

class Balance():

    balance = 0
    history = {}

    def __init__(self):
        print('-' * 10 + '  Начало операции  ' + '-' * 10)
        print('Создадим счёт')
        self.balance = int(input('Введите вашу сумму '))

        print(f'Поздравляем, Ваш счёт составляет {self.balance} рублей!')
        print('-' * 10 + '  Конец операции  ' + '-' * 10)
        print()

    def increase(self):
        print('-' * 10 + '  Начало операции  ' + '-' * 10)
        sum_in = int(input('Какую сумму желаете внести? '))
        self.balance += sum_in
        print(f'Прекрасно! Теперь Ваш счёт составляет {self.balance} рублей')
        print('-' * 10 + '  Конец операции  ' + '-' * 10)
        print()

    def decrease(self):
        print('-' * 10 + '  Начало операции  ' + '-' * 10)
        sum_out = int(input('Какую сумму желаете потратить? '))
        if sum_out <= self.balance:
            self.balance -= sum_out
            purchase = input('Введите название вашей покупки: ')
            self.history.update([(purchase, str(sum_out) + ' руб')])
        else:
            print('Извините, на счёте недостаточно средств.')
        print('-' * 10 + '  Конец операции  ' + '-' * 10)
        print()

    def my_history(self):
        obj_list = self.history.items()
        for item in obj_list:
            print(item)
        print('-' * 10 + '  Конец операции  ' + '-' * 10)
        print()

my_balance = Balance()
while True:
    print('0. Пересоздание счёта')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню ')
    if choice == '0':
        remake = input('Вы уверены, что хотите пересоздать счёт? y/n: ')
        if remake == 'y':
            my_balance = Balance()
        else:
            continue
    if choice == '1':
        my_balance.increase()
    elif choice == '2':
        my_balance.decrease()
    elif choice == '3':
        my_balance.my_history()
    elif choice == '4':
        print('Спасибо за обращение! Хорошего дня!')
        break
    else:
        print('Неверный пункт меню')
