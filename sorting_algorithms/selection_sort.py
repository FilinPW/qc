"""
Реализация алгоритма сортировки выбором (Selection Sort).
"""

def selection_sort(arr):
    """
    Сортировка массива методом выбора (Selection Sort).

    Args:
        arr: Список элементов для сортировки

    Returns:
        Отсортированный список
    """
    # Создаем копию массива, чтобы не изменять оригинальный
    sorted_arr = arr[:]
    n = len(sorted_arr)

    for i in range(n):
        # Находим индекс минимального элемента в оставшейся части массива
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        
        # Меняем местами текущий элемент с минимальным
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    
    return sorted_arr


if __name__ == "__main__":
    # Тестирование функции
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", test_array)
    sorted_array = selection_sort(test_array)
    print("Отсортированный массив:", sorted_array)