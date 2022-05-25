# В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
# Это могут быть функции консольного файлового менеджера,
#а так же программы мой счет и программы викторина

import os
import use_functions
import file_manager
import borndayforewer


def test_view_sys_info():
    assert file_manager.view_sys_info() == 'win32'
#
#
# def view_file():
#     file_list = []
#     for el in os.listdir():
#         if '.' in el:
#             file_list.append(el)
#     print(file_list)
#
#
# def view_dir():
#     dir_list = []
#     for el in os.listdir():
#         if '.' not in el:
#             dir_list.append(el)
#     print(dir_list)
#
#
# def view_sys_info():