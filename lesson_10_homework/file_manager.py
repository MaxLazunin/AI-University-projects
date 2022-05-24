import os
import sys
import shutil


def create():
    name = input('Введите название папки: ')
    if name in os.listdir():
        print('Данная папка уже существует в данной директории')
    else:
        os.mkdir(name)

def remove():
    name = input('Введите название папки: ')
    os.rmdir(name)
    print('Удаление завршено')

def copy():
    name = input('Выберете файл/папку: ')
    shutil.copytree(name,  f'{name}_copy')

def view():
    print(os.listdir())

def view_file():
    file_list = []
    for el in os.listdir():
        if '.' in el:
            file_list.append(el)
    print(file_list)

def view_dir():
    dir_list = []
    for el in os.listdir():
        if '.' not in el:
            dir_list.append(el)
    print(dir_list)

def view_sys_info():
    print(sys.platform)



def start_manager():
    work_trigger = 'y'
    while work_trigger =='y':
        start_menu_list = ['Создать папку', 'Удалить файл/папку', 'Копировать файл/папку', 'просмотр содержимого рабочей директории',
                      'Посмотреть только папки', 'Посмотреть только файлы', 'Просмотр информации об операционной системе', 'Создатель программы',
                      'Играть в викторину', 'Мой банковский счёт', 'Смена рабочей директории', 'Выход']
        print('-' * 10, 'Main menu', '-' * 10)
        for i in range(len(start_menu_list)):
            print(i, '-->', start_menu_list[i])
        choice = input('Выберете пункт меню: ')
        if choice == '0':
            create()
        elif choice == '1':
            remove()
        elif choice == '2':
            copy()
        elif choice == '3':
            view()
        elif choice == '4':
            view_dir()
        elif choice == '5':
            view_file()
        elif choice == '6':
            view_sys_info()
        elif choice == '7':
            view_sys_info()

        elif choice == '11':
            work_trigger = 'n'

        # work_trigger = input('Желаете продолжить работу с менеджером? y/n:  ')
    print('Спасибо, что воспользовались нашим продуктом!')




start_manager()