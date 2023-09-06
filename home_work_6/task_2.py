'''
Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
'''

from random import randint

min = int(input('Введите минимальный элемент диапазона: '))
max = int(input('Введите максимальный элемент диапазона: '))
lst_1 = [randint(-50, 50) for i in range(30)]
lst_2 = []
print(lst_1)

for i in lst_1:
    if i >= min and i<= max:
        print(i)
        lst_2.append(lst_1.index(i))

print(lst_2)