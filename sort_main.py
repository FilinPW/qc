#!/usr/bin/env python3
"""
Основной скрипт для сортировки чисел из текстового файла.
Поддерживает разные алгоритмы сортировки: пузырьком, быстрая сортировка и сортировка слиянием.
"""

import sys
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from utils import read_numbers_from_file


def main():
    if len(sys.argv) != 3:
        print("Использование: python sort_main.py <алгоритм> <имя_файла>")
        print("Алгоритмы: bubble (пузырьком), quick (быстрая сортировка), merge (слиянием), insertion (вставками)")
        sys.exit(1)

    algorithm = sys.argv[1].lower()
    filename = sys.argv[2]

    # Выбор алгоритма
    if algorithm == 'bubble':
        sort_func = bubble_sort
        sort_name = "Пузырьковая сортировка"
    elif algorithm == 'quick':
        sort_func = quick_sort
        sort_name = "Быстрая сортировка"
    elif algorithm == 'merge':
        sort_func = merge_sort
        sort_name = "Сортировка слиянием"
    elif algorithm == 'insertion':
        sort_func = insertion_sort
        sort_name = "Сортировка вставками"
    else:
        print(f"Неизвестный алгоритм: {algorithm}")
        print("Доступные алгоритмы: bubble, quick, merge, insertion")
        sys.exit(1)

    try:
        numbers = read_numbers_from_file(filename)
        print(f"Прочитано {len(numbers)} чисел из файла {filename}")
        print(f"Используется алгоритм: {sort_name}")
        
        if numbers:
            print("Исходные числа:", numbers)
            
            # Применяем выбранный алгоритм
            if algorithm == 'bubble':
                # Для пузырьковой сортировки нужно передать копию списка, т.к. она изменяет его на месте
                numbers_copy = numbers[:]
                sort_func(numbers_copy)
                result = numbers_copy
            else:
                # Быстрая сортировка, сортировка слиянием и сортировка вставками возвращают новый список
                result = sort_func(numbers)
                
            print("Отсортированные числа:", result)
        else:
            print("В файле не найдено корректных чисел для сортировки.")
            
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()