import math as m


def f_const(n = 1):
    return 1


def f_logn(n):
    steps2 = 0
    for i in range(int(m.log2(n))):
        steps2 += 1
    return steps2


def f_n2(n):
    steps3 = 0
    for i in range(n):
        for j in range(n):
            steps3 += 1
    return steps3


def f_2pown(n):
    steps4 = 0
    for i in range(2 ** n):
        steps4 += 1
    return steps4


a = int(input('Введите число n: '))
print(f_const(a))
print(f_logn(a))
print(f_n2(a))
print(f_2pown(a))
