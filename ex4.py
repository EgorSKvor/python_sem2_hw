# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
n = int(input('Enter num '))
lst = []
for i in range(-n, n + 1):
    lst.append(i)
nums = input('Enter nums ').split(' ')
mult = 1
for i in nums:
    mult = mult * lst[int(i)]

print(lst)
print(mult)
