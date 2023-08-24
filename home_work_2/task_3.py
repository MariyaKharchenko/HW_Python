'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

n = int(input('Введите число:'))

a = 2
b = 0
c = 0
our_list = []
while c<n:
    c = a**b
    our_list.append(c)
    b += 1
our_list.pop(-1)
print(our_list)