# Реализуйте алгоритм перемешивания списка.

from random import shuffle

def create_mixing_list(list_size):
    if list_size.isdigit() and int(list_size) > 1:
        list_size = int(list_size)
        result=[(i+1) for i in range(list_size)]
        print(f'Число элементов в списке = {list_size}\n Список:\n {result}')
        shuffle(result)
        print(f'Перемешанный список:\n {result}')
    else:
        print("Пожалуйста, введите число > 1")


def input_lenght():
    lenght = input('Введите число элементов для списка: ')
    create_mixing_list(lenght)

input_lenght()