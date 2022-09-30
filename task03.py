# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


n=input('Введите число элементов для n, чтобы задать список: ')
if n.isdigit() and int(n) > 0:
    n = int(n)
    result=[]
    for i in range(1, n+1):
        result.append((1+1/i)**i)
    print(f'Для n = {n}: {result}')
    sum = 0
    for i in range(len(result)):
        sum += result[i]
    print(f'Сумма чисел последовательности = {sum}')
else:
    print("Пожалуйста, введите число > 0")