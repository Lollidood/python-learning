'''https://github.com/artemegorof/modules_and_files/blob/main/module_05/lesson_03/step_05/tests'''
# Задача — написать функцию print_columns, которая открывает CSV-файл и выводит значения только из указанных колонок.

import csv


def print_columns(filename: str, columns: list[str]) -> None:

    with open(filename, encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        indexes = []
# ищем индекс колонки в заголовке
        for column in columns:
            if column in header:
                indexes.append(header.index(column))
            else:
                indexes.append(None)
# Если ни одна из указанных колонок не найдена — выводим сообщение
        if all(index is None for index in indexes):
            print("Указанные колонки не найдены.")
            return
# Формируем строку из нужных колонок
        for row in reader:
            result = []
            for index in indexes:
                if index is None:
                    result.append("N/A")
                # Колонка есть — добавляем значение
                else:
                    result.append(row[index])
            print(";".join(result))
