# Дан список целых чисел.
# Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. 
# Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.


list1 = []
import random
for i in range (10):
    n = random.randint(0,10)
    list1.append(n)
print("Список")
print (list1)
x = int(input("Введите  число x - "))
count = 0
for i in list1:
    if x == i:
        count += 1
if count > 0:
    print(f"Число {x} присутствует в списке в количестве - {count} ")
else :
   print(f"Число {x}  отсутствует: -1")