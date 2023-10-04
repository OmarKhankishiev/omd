import csv
from typing import Dict


def read_csv_file(filename: str) -> list:
    """
    Читает данные из CSV файла и возвращает их в виде списка списков.

    Args:
        filename (str): Имя CSV файла.

    Returns:
        list: Список списков с данными из CSV файла.
    """
    data = []
    with open(filename, newline="", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)
        for row in reader:
            data.append(row)
    return data


def read_department_hierarchy(filename: str) -> Dict[str, list]:
    """
    Читает CSV файл и создает иерархию команд.

    Args:
        filename (str): Имя CSV файла.

    Returns:
        dict: Словарь с иерархией команд.
    """
    department_hierarchy: Dict[str, list] = {}
    data = read_csv_file(filename)

    for row in data:
        department = row[1]
        section = row[2]

        if department not in department_hierarchy:
            department_hierarchy[department] = []
        department_hierarchy[department].append(section)

    return department_hierarchy


def print_department_hierarchy(department_hierarchy: Dict[str, list]) -> None:
    """
    Выводит иерархию команд на экран.

    Args:
        department_hierarchy (dict): Словарь с иерархией команд.
    """
    for department, sections in department_hierarchy.items():
        print(f"Департамент: {department}")
        print("Команды:")
        for section in set(sections):
            print(f"  - {section}")


def print_department_summary(department_data: Dict[str, dict]) -> None:
    """
    Выводит сводный отчет по департаментам на экран.

    Args:
        department_data (dict): Словарь с данными по департаментам.
    """
    for department, data in department_data.items():
        formatted_data = format_department_summary(data)
        print(f"Департамент: {department}")
        print(formatted_data)


def format_department_summary(data: dict) -> str:
    """
    Форматирует данные сводного отчета по департаментам.

    Args:
        data (dict): Словарь с данными по департаментам.

    Returns:
        str: Отформатированные данные.
    """
    count = data["count"]
    min_salary = data["min_salary"]
    max_salary = data["max_salary"]
    average_salary = data["total_salary"] / count

    formatted_data = (
        f"Численность: {count} сотрудников\n"
        f"З/п: Мин - {min_salary}, "
        f"Макс - {max_salary}, "
        f"Сред - {average_salary}\n "
    )

    return formatted_data


def calculate_department_summary(filename: str) -> Dict[str, dict]:
    """
    Читает CSV файл и создает сводный отчет по департаментам.

    Args:
        filename (str): Имя CSV файла.

    Returns:
        dict: Словарь с данными по департаментам.
    """
    department_data = {}
    data = read_csv_file(filename)

    for row in data:
        department = row[1]
        salary = float(row[5])

        if department not in department_data:
            department_data[department] = {
                "count": 0,
                "min_salary": salary,
                "max_salary": salary,
                "total_salary": 0
            }

        department_data[department]["count"] += 1
        if salary < department_data[department]["min_salary"]:
            department_data[department]["min_salary"] = salary
        if salary > department_data[department]["max_salary"]:
            department_data[department]["max_salary"] = salary
        department_data[department]["total_salary"] += salary

    return department_data


def save_department_summary_to_csv(department_data: Dict[str, dict],
                                   filename: str) -> None:
    """
    Сохраняет сводный отчет по департаментам в CSV файл.

    Args:
        department_data (dict): Словарь с данными по департаментам.
        filename (str): Имя CSV файла для сохранения.
    """
    with open(filename,
              mode="w",
              newline="",
              encoding="utf8") as summary_report_file:
        writer = csv.writer(summary_report_file, delimiter=';')
        writer.writerow([
            "Департамент",
            "Численность",
            "Минимальная зарплата",
            "Максимальная зарплата",
            "Средняя зарплата"
        ])

        for department, data in department_data.items():
            formatted_data = format_department_summary(data)
            writer.writerow([department, *formatted_data.split('\n')])

    print(f"Сводный отчет сохранен в файл '{filename}'")


if __name__ == "__main__":
    print("Меню:")
    print("1. Вывести иерархию команд")
    print("2. Вывести сводный отчет по департаментам")
    print("3. Сохранить сводный отчет в CSV файл")

    choice = input("Введите номер выбранной функции: ")
    file_path = input("Введите путь к файлу: ")

    if choice == "1":
        department_hierarchy = read_department_hierarchy(file_path)
        print_department_hierarchy(department_hierarchy)
    elif choice == "2":
        department_data = calculate_department_summary(file_path)
        print_department_summary(department_data)
    elif choice == "3":
        department_data = calculate_department_summary(file_path)
        save_department_summary_to_csv(department_data, "Summary_Report.csv")
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
