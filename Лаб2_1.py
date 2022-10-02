import numpy as np
print('Введите операцию с матрицей')
operation=input()
print('введите значения n(кол-во строк) и m(кол-во столбцов)')
    n1=int(input('n1='))
    m1=int(input('m1='))
#Ввод первоначальной матрицы 
a1=[]
for i in range(1, n1+1):
    a1.append([])
    for j in range(1, m1+1):
        a1[i-1].append(int(input()))
if operation=='Транспонирование':
    a11=np.array(a1)
    a111=a11.transpose()
    print(a111)
if operation=='*':
    n2=int(input('n2='))
    m2=int(input('m2='))
    a2=[]
    if m1==n2:
        #Ввод 2 первоначальной матрицы 
        for i in range(1, n2+1):
            a2.append([])
            for j in range(1, m2+1):
                a2[i-1].append(int(input()))
    print(np.matmul(a1,a2))
if operation=='Ранг':
    a11=np.array(a1)
    rang=np.linalg.matrix_rank(a11)
    print(rang)
