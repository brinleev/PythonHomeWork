#     Напишите рекурсивную функцию для возведения числа a в степень b.
# Разрешается использовать только операцию умножения.
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def degree_number(number,exp):
    if exp == 0:
        return 1
    return number * degree_number(number,exp-1)
number = int(input("Введите число - "))
exp = int(input("Введите степень числа - "))
print(f"{number}**{exp} = {degree_number(number,exp)}")