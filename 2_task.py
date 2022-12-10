#  Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


from functools import reduce


def sum_of_digits(arg):
    lst = [int(i) for i in arg if i != '.' and i != ',']
    result = reduce((lambda x, y: x + y), lst)
    return result


args_ = input('\nВведите число: ')
print(
    f'Результат суммирования цифр в числе {args_} равен {sum_of_digits(args_)}')