'''Задание 1
Транспонирование матриц'''
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
if operation=='транспонирование':
    #Вывод транспонированной матрицы
    for i in range(m1):
        s=[]
        for j in range(n1):
            s.append(a1[j][i])
        print(s)
'''Умножение матриц'''
if operation=='умножение':
    n2=int(input('n2='))
    m2=int(input('m2='))
    a2=[]
    if m1==n2:
        #Ввод 2 первоначальной матрицы 
        for i in range(1, n2+1):
            a2.append([])
            for j in range(1, m2+1):
                a2[i-1].append(int(input()))
        #Вывод результата
        for i in range(n1):
            s=[]
            for j in range(m2):
                sum=0
                for g in range(m1):
                    sum+=a1[i][g]*a2[g][j]
                s.append(sum)
            print(s)
                    
        
    else:
        print('Невозможно вычислить')
   


        
    
