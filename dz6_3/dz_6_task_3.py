import sys
from pathlib import Path
from colorama import init, Fore, Style
# включаємо colorama
init(autoreset=True)


def print_tree(directory, indent=""):
    """Виводимо вміст папки (папки синім, файли зеленим)."""
    for item in sorted(directory.iterdir()):
        if item.is_dir():
            # папка
            print(indent + Fore.BLUE + item.name + "/")
            # заходимо в підпапку глибше
            print_tree(item, indent + "    ")
        else:
            # файл
            print(indent + Fore.GREEN + item.name)


def main():
    # перевіряємо, що нам дали шлях як аргумент
    if len(sys.argv) < 2:
        print("Будь ласка, передайте шлях до директорії як аргумент.")
        print("Приклад: python dz_6_task_3.py /шлях/до/директорії")
        return

    path_str = sys.argv[1]
    directory = Path(path_str)


    # перевіряємо чи є шлях і, що це за директорія
    if not directory.exists():
        print(f"Шляху не існує: {directory}")
        return

    if not directory.is_dir():
        print(f"Це не директорія: {directory}")
        return

    # виводимо нашу структуру
    print_tree(directory)


if __name__ == "__main__":
    main()

#Перевірка: python dz6_3/dz_6_task_3.py /Users/sergzin/Documents/Neovercity/projects_neovercity/goit_pycore_hw_04/dz6_3/picture