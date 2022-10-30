import random as r


def list_in(x, y):
    for j in range(x):
        y.append(r.randrange(100))


n = int(input("Введите размер массива: "))
a = list()
list_in(n, a)
print(*a)
while True:
    act = 0
    for i in range(n):
        if (n-1) != i:
            if a[i] > a[i + 1]:
                act += 1
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
            else:
                continue
        else:
            break
    if act == 0:
        break
print(*a)
