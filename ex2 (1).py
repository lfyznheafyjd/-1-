import math as m
import random as r


def f_3n(n):
    mas = []
    steps1 = 0
    for i in range(n):
        mas.append(r.randrange(50))
        steps1 += 1
    for i in range(n):
        print(mas[i]," ",  end='')
        steps1 += 1
    max_v = mas[0]
    for i in range(n):
        steps1 += 1
        if mas[i] > max_v:
            max_v = mas[i]
    print("- max value: ",max_v)
    return steps1


def f_nlogn(n, x):
    mas = []
    t = x - 1
    steps2 = 0
    for i in range(n):
        mas.append(i)
    t += 1
    left = 0
    right = n - 1
    step = 1
    while step <= int(m.log2(n)):
        mid = (left + right) // 2
        if mas[mid] == t:
            steps2 += step
            break
        elif mas[mid] > t:
            right = mid
        elif mas[mid] < t:
            left = mid
        step += 1
        if step - 1 == int(m.log2(n)):
            steps2 += step
    return steps2


def f_nf(n):
    global steps4
    if n == 0:
        return 1
    steps4 += 1
    return f_nf(n - 1) * n


def f_n3(n):
    steps5 = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                steps5 += 1
    return steps5


def f_3logn(n, x):
    mas = []
    t = x - 1
    steps6 = 0
    for i in range(n):
        mas.append(i)
    for i in range(3):
        left = 0
        right = n - 1
        step = 1
        t += 1
        while step <= int(m.log2(n)):
            mid = (left + right) // 2
            if t == mas[mid]:
                steps6 += step
                break
            elif t > mas[mid]:
                left = mid
            elif t < mas[mid]:
                right = mid
            step += 1
            if step - 1 == int(m.log2(n)):
                steps6 += step
    return steps6


steps4 = 1
a = int(input("Введите число n: "))
b = int(input("Введите число x: "))
print(f_3n(a))
print(f_nlogn(a, b))
print(f_nf(a))
print(f_n3(a))
print(f_3logn(a, b))