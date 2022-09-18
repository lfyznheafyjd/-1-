#Задание #1
'''
a, b=int(input()), int(input())
print(a-b)
c, d=input(), input()
print(c+d)
e, f=list(input().split()), list(input().split())
print(e+f)
g, h=tuple(input()), tuple(input())
print(len(g), len(h))
'''

#Задание #2
from math import*
print('Выберите функцию(введите номер функции)')
print('1.Сложение')
print('2.Вычитание')
print('3.Умножение')
print('4.Деление')
print('5.Возведение в степень')
print('6.Логарифм')
print('7.Округление в большую сторону')
print('8.Округление в меньшую сторону')
func=int(input())
print('Введите первый элемент')
while True:
    a=input()
    if a.isdigit() or (a.count('.')==1 and a[0]!='.') or (a.count('-')==1 and a[0]=='-' and a[1]!='.'):
        a = float(a)
        break
    else:
        print('Введенный элемент не является числом')
if func!=7 and func!=8:
    print('Введите второй элемент')    
    while True:
        b=input()
        if b.isdigit() or (b.count('.')==1 and b[0]!='.') or (b.count('-')==1 and b[0]=='-' and b[1]!='.'):
            b = float(b)
            break
        else:
            print('Введенный элемент не является числом')

#Сложение
if func==1:
    print(a+b)
#Вычитание
if func==2:
    print(a-b)
#Умножение
if func==3:
    print(a*b)
#Деление
if func==4:
    print(a/b)
#Возведение в степень
if func==5:
    print(a**b)
#Логарифм
if func==6:
    print(log(b)/log(a))
#Округление
if func==7 or func==8:
    print('Укажите кол-во знаков после запятой, до которого вы хотите округлить число')
    n=int(input())
    if a>=0:
        a=str(a)
        #вспомогательная переменнная
        h=1
        while True:
            if a[h]=='.':
                m=h+1
                break
            else:
                h+=1
        n=m+n
        if len(a)==m+1 and a[-1]=='0':
            print(round(float(a)))
        elif len(a)>n:
            a=a[0:n]
            a=float(a)
            if func==7:
                print(a+10**((n-m)*(-1)))
            else:
                print(a)
        elif len(a)==n:
            print(float(a))
        else:
            print('n не должен быть больше чем знаков после запятой')
    else:
        a=str(a)
        #Вспомогательная переменная
        h=2
        while True:
            if a[h]=='.':
                m=h+1
                break
            else:
                h+=1
        n=m+n
        if len(a)==m+1 and a[-1]=='0':
            print(round(float(a)))
        elif len(a)>n:
            a=a[0:n]
            a=float(a)
            if func==7:
                print(a)
            else:
                print(a-10**((n-m)*(-1)))
        elif len(a)==n:
            print(float(a))

        
