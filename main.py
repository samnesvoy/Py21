# file_object=open(file_name,mode_open)
# file_object - объект содержащий информацию о файле
#       и инструменты работы с ним
# open - функция открытия файла (внезапно, правда?)
# file_name - имя файла(путь к файлу, может быть
#   относительным(относительно файла в котором написан этот код)
#   и абсолютным (точкой отсчета является корень диска)
# mode_open - режим открытия файла
# w - открываем файл для записи.
#   Если файл не существует - будет создан и открыт.
#   Если файл существует - будет очищен и открыт.
# r - открываем файл для чтения.
#   Если файл не существует - ошибка открытия.
#   Если файл существует - будет открыт и курсор чтения выставлен в начало.
# a - открываем файл для добавления.
#   Если файл не существует - будет создан и открыт.
#   Если файл существует - будет открыт и курсор чтения выставлен в конец.
# file = open('test.txt', 'r')
# # file.write('mama mila window\n')
# print(file.readlines())
# # print(file.readline())
# # file.close()
# file = open('test.txt', 'w')
# file.write('blablabla\n')


with open('test2.txt') as f:
    print(f.read())

with open('test2.txt', 'w') as f:
    f.write('\nNew string')
with open('test2.txt') as f:
    print(f.read())
# with open("test2.txt", "a") as fileHandler:
#     fileHandler.write("\nHello Again!")
#
# fileHandler1 = open("test2.txt")
# print(fileHandler1.read())
