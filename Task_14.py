#  Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
# не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8

n = int(input("Введите диапазон n - "))
i = 0
while 2 ** i <= n:
    print(2 ** i, end= "    ")
    i += 1