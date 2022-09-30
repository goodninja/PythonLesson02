# Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(f'Список элементов: {numbers}')

def get_nums(numbers):
    count = 0 
    for element in numbers:
        count += 1
    return count
print('Количество элементов: ', get_nums(numbers))

x = int(input('Введите позицию для первого элемента: '))
y = int(input('Введите позицию для второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x - 1]*numbers[y - 1]
print(f'Произведение элементов на указанных позициях: {numbers[x - 1]} * {numbers[y - 1]} =', mult)