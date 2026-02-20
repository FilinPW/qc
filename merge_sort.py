#!/usr/bin/env python3
"""
Модуль для сортировки слиянием
"""

def merge_sort(arr):
    """
    Реализация сортировки слиянием (merge sort)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """
    Вспомогательная функция для слияния двух отсортированных массивов
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result