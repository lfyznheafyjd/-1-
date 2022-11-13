def insertion_sort(block):
    for i in range (1, len (block)):
        var = block[i]
        j = i - 1
        while (j >= 0 and var < block[j]):
            block[j + 1] = block[j]
            j-=1
        block[j + 1] = var
def block_sort(a):
    # Находим максимальное значение в списке. Затем используем длину списка, чтобы определить, какое значение в списке попадет в какой блок
    max_zn = max(a)
    size = max_zn/len(a)

    # Создаем n пустых блоков, где n равно длине входного списка
    b= []
    for x in range(len(a)):
        b.append([]) 

    # Помещаем элементы списка в разные блоки на основе size
    for i in range(len(a)):
        j = int (a[i] / size)
        if j != len (a):
            b[j].append(a[i])
        else:
            b[len(a) - 1].append(a[i])

    # Сортируем элементы внутри блоков с помощью сортировки вставкой
    for z in range(len(a)):
        insertion_sort(b[z])
            
    # Объединяем блоки с отсортированными элементами в один список
    sort_m = []
    for x in range(len (a)):
        sort_m = sort_m + b[x]
    return sort_m
def main():
    a=list(map(int, input().split()))
    sorted_list = block_sort(a)
    print(sorted_list)
main()
