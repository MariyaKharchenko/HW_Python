'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных 
числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя 
делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
'''

x = 1
y = 1

S = int(input('Введите сумму чисел:'))
P = int(input('Введите произведение чисел:'))

while x+y != S and x*y != P:
    
    if P%x != 0:
        x +=1

    while P%y != 0 or P/y != x:
        y +=1

    
    if x+y != S:
        x += 1
        y = 1
    

print(x, y)
    
        