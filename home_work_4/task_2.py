'''
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
причём кусты высажены только по окружности. Таким образом, у каждого куста есть 
ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать 
за один заход собирающий модуль, находясь перед некоторым кустом заданной 
во входном файле грядки.
'''

from random import randint


n = int(input('Введите кол-во кустов на грядке:'))
garden_bed = []
maximum_berries = 0
berries = 0

for i in range(n):
    garden_bed.append(randint(1, 10))

print(garden_bed)

for i in range(n):
    if i == n-1:
        berries = garden_bed[0]+garden_bed[-1]+garden_bed[-2]
    elif i == 0:
        berries = garden_bed[0]+garden_bed[-1]+garden_bed[1]
    else:
        berries = garden_bed[i]+garden_bed[i-1]+garden_bed[i+1]
    if berries > maximum_berries:
        maximum_berries = berries
print(maximum_berries)