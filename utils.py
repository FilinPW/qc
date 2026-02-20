#!/usr/bin/env python3
"""
Утилиты для работы с файлами
"""

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