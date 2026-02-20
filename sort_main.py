#!/usr/bin/env python3
"""
Основной скрипт для сортировки чисел из текстового файла.
Поддерживает разные алгоритмы сортировки: пузырьком и быстрая сортировка.
"""

import sys


def bubble_sort(arr):
    """
    Реализация сортировки пузырьком
    """
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            # Меняем местами, если текущий элемент больше следующего
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def quick_sort(arr):
    """
    Реализация быстрой сортировки (quicksort)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def read_numbers_from_file(filename):
    """
    Чтение чисел из файла
    """
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:  # Проверяем, что строка не пустая
                try:
                    number = int(line)
                    numbers.append(number)
                except ValueError:
                    print(f"Предупреждение: '{line}' не является целым числом, пропущено")
    return numbers


def main():
    if len(sys.argv) != 3:
        print("Использование: python sort_main.py <алгоритм> <имя_файла>")
        print("Алгоритмы: bubble (пузырьком), quick (быстрая сортировка)")
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
    else:
        print(f"Неизвестный алгоритм: {algorithm}")
        print("Доступные алгоритмы: bubble, quick")
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
                # Быстрая сортировка возвращает новый список
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