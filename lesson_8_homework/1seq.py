'''
(МОДУЛЬ 1) Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
'''

count = int(input('Введите колличество элементво списка : '))
my_list = []
for i in range(count):
    my_list.append(int(input(f'Введите {i+1} элемент: ')))
print(f'Исходный список {my_list}')
my_list.sort()
print(f'Список после сортировки {my_list}')
