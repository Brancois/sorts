def bubble_sort(list):
    n = len(list)
    for i in range(n - 1, 0, -1):
        for j in range(n - 1, n - i - 1, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
    return list


def insert_sort(list):
    for i in range(len(list) - 1, 0, -1):
        value = list[i]
        j = i - 1
        while j >= 0 and list[j] > value:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = value
    return list


def select_sort(list):
    for i in range(len(list) - 1, 0, -1):
        maximo = i
        for j in range(i - 1, -1, -1):
            if list[j] > list[maximo]:
                maximo = j
        list[i], list[maximo] = list[maximo], list[i]
    return list


def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list


# Maneras de aplicar los sorts
list = [25, 72, 85, 10, 5, 77, 16]


def sort():
    opciones = ['Bubble sort', 'Insertion sort',
                'Selection sort', 'Merge sort']
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")
    op = input('Cual sort desea usar?: ')
    if op == '1':
        print("Bubble Sort:", bubble_sort(list.copy()))
    elif op == '2':
        print("Insertion Sort:", insert_sort(list.copy()))
    elif op == '3':
        print("Selection Sort:", select_sort(list.copy()))
    elif op == '4':
        print("Merge Sort:", merge_sort(list.copy()))
    else:
        print('Disculpa, esa opcion no esta...')


sort()
