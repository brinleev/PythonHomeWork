# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.

# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10
# (*) Усложнение. Если в списке несколько чисел "равноблизких" к заданному числу X, 
# выводим все числа в отсортированном виде (по возрастанию)

list1 = []
import random
for i in range (10):
    n = random.randint(0,10)
    list1.append(n)
print("Список")
print (list1)
x = int(input("Введите  число x - "))
mindifference = abs(x - list1[0])
count = 0
for i in range(1,len(list1)):
    difference = abs(x - list1[i])
    if difference <= mindifference:
        mindifference = difference
        count = i
print('Ближайшее число ->', list1[count], end='\n')	

