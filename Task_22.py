# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры.

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

list1 = []
import random
for i in range (10):
    n = random.randint(0,50)
    list1.append(n)
print("Список 1")
print (*list1, sep='  ')
list2 = []
import random
for i in range (10):
    n = random.randint(0,50)
    list2.append(n)
print("Список 2")
print (*list2, sep='  ')
list3=[]
for i in list1:
    if i in list2 and i not in list3:
        list3.append(i) 
if len(list3) == 0:
    print("Повторяющихся чисел нет") 
else:
    list3.sort()
    print("Результат")
    print(*list3, sep='  ')  
   
  
    