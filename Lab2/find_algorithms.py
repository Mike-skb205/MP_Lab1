## @Algorithms
#  Here are declared all the search engines, such as Binary and Sumple

## def simple_search(arr, key)
## def binary_search(arr, start, end, key)
## heapify(nums, heap_size, root_index) - used by heap_sort()
## def heap_sort(nums)

"""Простой поиск"""
def simple_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            #print("Find alg***", arr[i], " ", key, "***Find alg")
            return i
    return -1

"""Бинарный поиск"""
def binary_search(data, start, end, elem):
    if start > end:
        return -1
    while start <= end:
        middle = start + ( end - start) // 2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            end = middle - 1
        else:
            start = middle + 1
        return -1

def binary_search_testCode(arr, start, end, key):
    if start > end:
        return -1
    middle = start + (end - start) // 2

    if arr[middle] == key:
        return middle
    if arr[middle] > key:
        return binary_search(arr, start, middle - 1, key)

    return binary_search(arr, middle + 1, end, key)

"""Пирамидальная сортировка для использования позднее для бинарного поиска"""
def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — это допустимый индекс, а элемент больше,
    # чем текущий наибольший, то мы обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое и для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент уже не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # Создаём Max Heap из списка
    # 2-й аргумент означает остановку алгоритма перед элементом -1, то есть
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
