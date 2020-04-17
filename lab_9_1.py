from time import time
from random import randint


# Сортування за зростанням(яке в кожній функції є першим) та спаданням знаходяться в 1 функції з поверненням змінних до початкових значень
def bubbleSort(arr):
    new_arr = arr[:]

    compare_count = 0
    exchange_сount = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            compare_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                exchange_сount += 2
    print("Сортування за зростанням: ", arr)
    print('Кількість порівнянь послідовності зростання: ', compare_count)
    print('Кількість перестановок послідовності зростання: ', exchange_сount)

    compare_count = 0
    exchange_сount = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            compare_count += 1
            if new_arr[j] < new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
                exchange_сount += 2
    print("Сортування за спаданням: ", new_arr)
    print('Кількість порівнянь послідовності спадання:', compare_count)
    print('Кількість перестановок послідовності спадання: ', exchange_сount)


def selectionSort(arr):
    new_arr = arr[:]

    compare_count = 0
    exchange_сount = 0
    for i in range(len(arr)):

        min_idx = i
        for j in range(i + 1, len(arr)):
            compare_count += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        exchange_сount += 2

    print("Сортування за зростанням: ", arr)
    print('Кількість порівнянь послідовності зростання: ', compare_count)
    print('Кількість перестановок послідовності зростання: ', exchange_сount)

    compare_count = 0
    exchange_сount = 0
    for i in range(len(new_arr)):

        min_idx = i
        for j in range(i + 1, len(new_arr)):
            compare_count += 1
            if new_arr[min_idx] < new_arr[j]:
                min_idx = j
        new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]
        exchange_сount += 2

    print("Сортування за спаданням: ", new_arr)
    print('Кількість порівнянь послідовності спадання: ', compare_count)
    print('Кількість перестановок послідовності спадання: ', exchange_сount)


def insertionSort(arr):
    new_arr = arr[:]
    compare_count = 0
    exchange_count = 0

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            compare_count += 2
            arr[j + 1] = arr[j]
            exchange_count += 1
            j -= 1
        compare_count += 2
        arr[j + 1] = key
        exchange_count += 2
    print("Сортування за зростанням: ", arr)
    print('Кількість порівнянь послідовності зростання: ', compare_count)
    print('Кількість перестановок послідовності зростання: ', exchange_count)

    compare_count = 0
    exchange_count = 0

    for i in range(1, len(new_arr)):

        key = new_arr[i]
        j = i - 1

        while j >= 0 and key > new_arr[j]:
            compare_count += 2
            new_arr[j + 1] = new_arr[j]
            exchange_count += 1
            j -= 1
        compare_count += 2
        new_arr[j + 1] = key
        exchange_count += 2
    print("Сортування за спаданням: ", arr)
    print('Кількість порівнянь послідовності зростання: ', compare_count)
    print('Кількість перестановок послідовності зростання: ', exchange_count)


def cocktailSort(arr):
    new_arr = arr[:]
    compare_count = 0
    exchange_count = 0
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:

        swapped = False

        for i in range(start, end):
            compare_count += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                exchange_count += 2
                swapped = True

        if not swapped:
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            compare_count += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                exchange_count += 2
                swapped = True

        start = start + 1
    print("Сортування за зростанням: ", arr)
    print('Кількість порівнянь послідовності зростання: ', compare_count)
    print('Кількість перестановок послідовності зростання: ', exchange_count)

    compare_count = 0
    exchange_count = 0
    n = len(new_arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:

        swapped = False

        for i in range(start, end):
            compare_count += 1
            if new_arr[i] < new_arr[i + 1]:
                new_arr[i], new_arr[i + 1] = new_arr[i + 1], arr[i]
                exchange_count += 2
                swapped = True

        if not swapped:
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            compare_count += 1
            if new_arr[i] < new_arr[i + 1]:
                new_arr[i], new_arr[i + 1] = new_arr[i + 1], new_arr[i]
                exchange_count += 2
                swapped = True

        start = start + 1
    print("Сортування за спаданням: ", new_arr)
    print('Кількість порівнянь послідовності спадання: ', compare_count)
    print('Кількість перестановок послідовності спадання: ', exchange_count)


def shellSort(arr):
    new_arr = arr[:]
    compare_count = 0
    exchange_count = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                compare_count += 2
                arr[j] = arr[j - gap]
                exchange_count += 1
                j -= gap

            arr[j] = temp
            exchange_count += 2
        gap //= 2

    print("Сортування за зростанням: ", arr)
    print('Кількість порівнянь послідовності зростання: ', compare_count)
    print('Кількість перестановок послідовності зростання: ', exchange_count)

    compare_count = 0
    exchange_count = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j >= gap and new_arr[j - gap] < temp:
                compare_count += 2
                new_arr[j] = new_arr[j - gap]
                exchange_count += 1
                j -= gap

            new_arr[j] = temp
            exchange_count += 2
        gap //= 2

    print("Сортування за спаданням: ", new_arr)
    print('Кількість порівнянь послідовності спадання: ', compare_count)
    print('Кількість перестановок послідовності спадання: ', exchange_count)


def heapify_growth(arr, n, i, exchange_count, compare_count):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    compare_count += 2
    if l < n and arr[i] < arr[l]:
        largest = l
        exchange_count += 1
    compare_count += 2
    if r < n and arr[largest] < arr[r]:
        largest = r
        exchange_count += 1
    compare_count += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        exchange_count += 2
        exchange_count, compare_count = heapify_growth(arr, n, largest, compare_count, exchange_count)
    return compare_count, exchange_count


def heapify_decrease(arr, n, i, compare_count, exchange_count):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    compare_count += 2
    if l < n and arr[i] > arr[l]:
        largest = l
        exchange_count += 1
    compare_count += 2
    if r < n and arr[largest] > arr[r]:
        largest = r
        exchange_count += 1
    compare_count += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        exchange_count += 2
        exchange_count, compare_count = heapify_decrease(arr, n, largest, compare_count, exchange_count)
    return compare_count, exchange_count


def heapSort(arr):
    new_arr = arr[:]
    n = len(arr)

    compare_count = 0
    exchange_count = 0
    heapify_growth(arr, n, 0, compare_count, exchange_count)
    for i in range(n, -1, -1):
        exchange_count, compare_count = heapify_growth(arr, n, i, compare_count, exchange_count)

    compare_count += 1
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        exchange_count += 2
        heapify_growth(arr, i, 0, compare_count, exchange_count)
    print("Сортування за зростанням: ", arr)
    print('Кількість порівнянь послідовності зростання: ', compare_count)
    print('Кількість перестановок послідовності зростання: ', exchange_count)

    n = len(new_arr)
    compare_count = 0
    exchange_count = 0
    heapify_decrease(new_arr, n, 0, compare_count, exchange_count)
    for i in range(n, -1, -1):
        exchange_count, compare_count = heapify_decrease(new_arr, n, i, compare_count, exchange_count)

    for i in range(n - 1, 0, -1):
        new_arr[i], new_arr[0] = new_arr[0], new_arr[i]
        heapify_decrease(new_arr, i, 0, compare_count, exchange_count)

    print("Сортування за спаданням: ", new_arr)
    print('Кількість порівнянь послідовності спадання: ', compare_count)
    print('Кількість перестановок послідовності спадання: ', exchange_count)


# Введення послідовності
# При довжині послідовності у 100 000 значень програма видає лише вихідну послідовність і припиняє роботу,
# тому зменшено до 10000
arr = []
if len(input(
        "Чи хочете Ви ввести до 30 значень самостійно?(Інші будуть введені рандомом)"
        "\nНатисніть *Enter* для рандомної генерації та введіть що-небудь"
        " для введення власних значень: ")) > 0:
    while True:
        elements_count = int(input("Скільки значень ви хочете ввести: "))
        if elements_count <= 30:
            arr += ([int(input("Введіть значення: ")) for i in range(elements_count)])
            arr += ([randint(0, 10000) for i in range(10000 - elements_count)])
            break
        else:
            print("Кількість має бути до 30!")
else:
    arr += ([randint(0, 10000) for i in range(10000)])
print("Вихідна послідовність: \n", arr)
print()
print("***БУЛЬБАШКОВЕ СОРТУВАННЯ***")
print()
tic = time()
bubbleSort(arr[:])
toc = time()
print("Час виконання сортування бульбашкою: ", (toc - tic))
print()
print("***СОРТУВАННЯ ВИБОРОМ***")
print()
tic = time()
selectionSort(arr[:])
toc = time()
print("Час виконання сортування вибором: ", (toc - tic))
print()
print("***СОРТУВАННЯ ВСТАВКАМИ***")
print()
tic = time()
insertionSort(arr[:])
toc = time()
print("Час виконання сортування вставкою: ", (toc - tic))
print()
print("***СОРТУВАННЯ КОКТЕЙЛЕМ***")
print()
tic = time()
cocktailSort(arr[:])
toc = time()
print("Час виконання сортування коктейлем: ", (toc - tic))
print()
print("***СОРТУВАННЯ ШЕЛЛА***")
print()
tic = time()
shellSort(arr[:])
toc = time()
print("Час виконання сортування Шелла: ", (toc - tic))
print()
print("***СОРТУВАННЯ ПІРАМІДОЮ***")
print()
tic = time()
heapSort(arr[:])
toc = time()
print("Час виконання сортування пірамідою: ", (toc - tic))
