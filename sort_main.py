#!/usr/bin/env python3
"""
Основной скрипт для сортировки чисел из текстового файла.
Поддерживает разные алгоритмы сортировки: пузырьком, быстрая сортировка и сортировка слиянием.
"""

import sys
import time
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from utils import read_numbers_from_file


def run_all_algorithms(numbers):
    """Запускает все алгоритмы сортировки и выводит время выполнения для каждого."""
    algorithms = [
        ('Пузырьковая сортировка', bubble_sort),
        ('Быстрая сортировка', quick_sort),
        ('Сортировка слиянием', merge_sort),
        ('Сортировка вставками', insertion_sort)
    ]
    
    print("Запуск всех алгоритмов сортировки последовательно...")
    print("-" * 50)
    
    for name, func in algorithms:
        numbers_copy = numbers[:]
        start_time = time.time()
        
        if name == 'Пузырьковая сортировка':
            # Для пузырьковой сортировки нужно передать копию списка, т.к. она изменяет его на месте
            func(numbers_copy)
            result = numbers_copy
        else:
            # Остальные алгоритмы возвращают новый список
            result = func(numbers_copy)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"{name}: {execution_time:.6f} секунд")
        
        # Проверка правильности сортировки
        is_sorted = all(result[i] <= result[i + 1] for i in range(len(result) - 1))
        print(f"  Результат корректен: {is_sorted}")
        print()


def main():
    if len(sys.argv) < 2:
        print("Использование: python sort_main.py <алгоритм> <имя_файла>")
        print("Или: python sort_main.py all <имя_файла> - для запуска всех алгоритмов")
        print("Алгоритмы: bubble (пузырьком), quick (быстрая сортировка), merge (слиянием), insertion (вставками), all (все алгоритмы)")
        sys.exit(1)

    algorithm = sys.argv[1].lower()
    filename = sys.argv[2] if len(sys.argv) > 2 else None
    
    if algorithm == 'all':
        if not filename:
            print("Для запуска всех алгоритмов укажите имя файла.")
            sys.exit(1)
        
        try:
            numbers = read_numbers_from_file(filename)
            print(f"Прочитано {len(numbers)} чисел из файла {filename}")
            print()
            
            if numbers:
                print("Исходные числа:", numbers)
                print()
                
                run_all_algorithms(numbers)
            else:
                print("В файле не найдено корректных чисел для сортировки.")
                
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден.")
            sys.exit(1)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            sys.exit(1)
        return

    if not filename:
        print("Использование: python sort_main.py <алгоритм> <имя_файла>")
        print("Или: python sort_main.py all <имя_файла> - для запуска всех алгоритмов")
        print("Алгоритмы: bubble (пузырьком), quick (быстрая сортировка), merge (слиянием), insertion (вставками), all (все алгоритмы)")
        sys.exit(1)

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
        print("Доступные алгоритмы: bubble, quick, merge, insertion, all")
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