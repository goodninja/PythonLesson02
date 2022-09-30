# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


num = input('Введите вещественное число для вывода суммы его чисел: ')
if num[0] == '-' or num[0] == '+':
    num = num[1:]
if '.' in num:
    num = num.split(".")
elif ',' in num:
    num = num.split(",")
num_result = ''
num_result = num_result.join(num)
if num_result.isdigit():
    result=0
    for i in range(len(num_result)):
        result += int(num_result[i])
    print(f'Сумма цифр данного вещественного числа = {result}')
else:
    print("Введены не верные данные")
