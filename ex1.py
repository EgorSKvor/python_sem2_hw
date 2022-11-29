# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 0,56 -> 11

num = input('Enter num ').split(',')
x_int = int(num[1])
summ = 0
while (x_int != 0):
    summ = summ + x_int % 10
    x_int = x_int // 10
print("Сумма цифр числа равна: ", summ)
