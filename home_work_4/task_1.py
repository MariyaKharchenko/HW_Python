'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые 
встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
'''

from random import randint
n = int(input('Введите число: '))
m = int(input('Введите число: '))

arr_1 = []
arr_2 = []

for i in range(n):
    arr_1.append(randint(0, 100))

for i in range(m):
    arr_2.append(randint(0, 100))

print(arr_1)
print(arr_2)

arr_1 = set(arr_1)
arr_2 = set(arr_2)

#print(arr_1)
#print(arr_2)

print(sorted(arr_1.intersection(arr_2)))