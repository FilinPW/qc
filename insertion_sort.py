#!/usr/bin/env python3
"""
Реализация алгоритма сортировки вставками (Insertion Sort).
"""


def insertion_sort(arr):
    """
    Сортировка вставками. Возвращает новый отсортированный список,
    не изменяя исходный.
    
    Args:
        arr: Список для сортировки
        
    Returns:
        Новый отсортированный список
    """
    # Создаем копию массива, чтобы не изменять оригинальный
    sorted_arr = arr[:]
    
    # Проходим по всем элементам, начиная со второго
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]  # Текущий элемент для вставки
        j = i - 1  # Индекс предыдущего элемента
        
        # Перемещаем элементы, которые больше ключа, на одну позицию вперед
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        
        # Вставляем ключ на правильное место
        sorted_arr[j + 1] = key
    
    return sorted_arr


if __name__ == "__main__":
    # Пример использования
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", test_list)
    sorted_list = insertion_sort(test_list)
    print("Отсортированный список:", sorted_list)