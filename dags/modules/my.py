def my() -> None:
    # import os
    # for f in os.listdir("opt/airflow/dags"):
    #     print(f)
    print('hi!')
    import os

    import pathlib
    from pathlib import Path

    # Задаем относительный путь с помощью Path!
    path = Path("files", "info", "docs.txt")

    ## выведем значение переменной path:
    print('относительный путь - ', str(path))

    # Задаем абсолютный путь с помощью Path
    # cwd() — возвращает путь к рабочей директории
    # home() — возвращает путь к домашней директории
    # Полученную строку, содержащую путь к рабочей или домашней директории,
    # объединим с недостающими участками пути при инициализации объекта класса Path :
    # Пример 1: с использованием функции cwd():

    # Получаем строку, содержащую путь к рабочей директории:
    dir_path = pathlib.Path.cwd()
    # Объединяем полученную строку с недостающими частями пути
    path = Path(dir_path, 'homework.csv')

    # выведем значение переменной path:
    print(dir_path, str(path))

    # Пример2: с использованием функции home():
    # Получаем строку, содержащую путь к домашней директории:
    dir_path = pathlib.Path.home()

    # Объединяем полученную строку с недостающими частями пути
    path = Path(dir_path, 'files', 'info', 'docs.txt')

    # Выведем значение переменной path:
    print(str(path))
    #print('/opt/airflow/dags

