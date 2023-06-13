#     Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def sum_numbers(summand1,summand2):
    if summand1 == 0:
        return summand2
    return sum_numbers( summand1-1, summand2 +1)

summand1 = int(input("Введите первое неотрицительное число - "))
summand2 = int(input("Введите второе неотрицательно число - "))
if summand1 < 0 or summand2 < 0:
    print("Введите положительные числа")
else:
    print (F"Сумма - {sum_numbers(summand1,summand2)}")   