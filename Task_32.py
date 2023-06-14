#     Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

def list_generator(a,b,c):
    import random
    list = [random.randint(a,b) for i in range (c)]
    return list
def index_determinant(list, min_range, max_range):
    list1 = []
    listi = []
    for i in range(len(list)-1):
        if list[i] > min_range and list[i] < max_range:
            listi.append(i)
            listi.append(list[i])
            list2 = tuple(listi)
            list1.append(list2)
        listi = []
    return list1    

print("Список:")
list = list_generator(0,100,10)
print (list, sep='  ')
print("Введите пределы через пробел: ")
print("нижний предел")
print("верхний предел")
min_range,max_range = map(int, input().split())
print(index_determinant(list, min_range, max_range))