#!/usr/bin/env python3
"""
Скрипт для сортировки чисел из текстового файла методом быстрой сортировки.
Числа должны быть записаны в столбик в файле.
"""

import sys


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
    if len(sys.argv) != 2:
        print("Использование: python quick_sort.py <имя_файла>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        numbers = read_numbers_from_file(filename)
        print(f"Прочитано {len(numbers)} чисел из файла {filename}")
        
        if numbers:
            print("Исходные числа:", numbers)
            sorted_numbers = quick_sort(numbers)
            print("Отсортированные числа:", sorted_numbers)
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