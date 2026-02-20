#!/usr/bin/env python3
"""
Скрипт для сортировки чисел из текстового файла методом пузырька.
Числа должны быть записаны в столбик в файле.
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
        print("Использование: python bubble_sort.py <имя_файла>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        numbers = read_numbers_from_file(filename)
        print(f"Прочитано {len(numbers)} чисел из файла {filename}")
        
        if numbers:
            print("Исходные числа:", numbers)
            bubble_sort(numbers)
            print("Отсортированные числа:", numbers)
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