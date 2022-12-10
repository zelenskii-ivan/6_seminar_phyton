
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


my_list = [2, 3, 4, 5, 6]
res_list = []
half_steps = len(my_list) // 2

# Было
# if len(my_list) % 2 != 0:
#     half_steps += 1
# for i in range(half_steps):
#     res_list.append(my_list[i] * my_list[-i - 1])

# Стало

if len(my_list) % 2 != 0:
    half_steps += 1
res_list = [my_list[x] * my_list[-x - 1] for x in range(half_steps)]

print(res_list)