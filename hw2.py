# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('Введите вещественное число: ')
# sum_numbers = 0
# for i in number:
#     if i != '.':
#        sum_numbers += int(i)
# print(f'Сумма цифр числа {number} равна {sum_numbers}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# number_N = int(input("Введите число: "))
# list = []
# for i in range(1, number_N+1):
#     if(i <= number_N):
#        list.append(i)

# res = 1
# for i in list:
#     res *= i
#     print(res, end = " ")

# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите целое число = '))              
# sum = 0
# for i in range(1, n + 1):
#     print(i, ')', (1 + 1/i)**i)
#     sum = sum + ((1 + 1/i)**i)
# print('\nСумма:', sum, '\n')


# Реализуйте алгоритм перемешивания списка.

import random
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = random.sample(list, len(list))
print ('\n', str(list), ' получаем случайный список ', str(result), '\n')
