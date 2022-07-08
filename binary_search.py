# Бинарный поиск, сложность: O(log n)
def binary_search(list, item):      
    low = 0                         # крайний наименьший элемент
    high = len(list) - 1            # крайний наибольший элемент

    while low <= high:              # пока эта чаcть не сократиться до одного элемента
        mid = (low + high) // 2     # провереяем средний элемент
        guess = list[mid]

        if guess == item:           # значение найдено
            return mid
        if guess > item:            # много
            high = mid - 1
        else:                       # мало
            low = mid + 1
    return None                     # Значения не существет

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))    # Вернет 4 так как 9 это элемент под индексом 4
