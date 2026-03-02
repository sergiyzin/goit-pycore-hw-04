# Робимо функцію, яка читає файл з зп і рахує її: загальну суму та середню зп
def total_salary(path: str) -> tuple[int, float]:

    # в total складаємо всі зп
    total = 0
    # count – кількість програмістів, яких рахуємо
    count = 0

    try:
        # відкриваємо файл через with (дістати рядки в коді)
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # З одного рядка витягємо зп
                line = line.strip()
                if not line:
                    continue

                try:
                    # рядок у форматі: "ім'я прізвище,сума"
                    name, salary_str = line.split(",")

                    # перетворюємо зп з рядка в число
                    salary = int(salary_str)
                except ValueError:
                    # якщо немає коми або не число, то пропускаємо такий рядок і йдемо далі
                    continue

                # додаємо зп до загальної суми
                total = total + salary
                # збільшуємо кількість записів
                count = count + 1

        # якщо є хоча б 1 запис, тоді рахуємо середню зп, а в іншому випадку повертаємо 0, щоб не ділити на 0
        average = total / count if count > 0 else 0

        # повертаємо кортеж: (загальна сума, середня зп)
        return total, average

    except FileNotFoundError:
        # якщо файл не був знайдений, то повертаємо нулі
        return 0, 0

if __name__ == "__main__":
    # /Users/sergzin/Documents/Neovercity/projects_neovercity/goit_pycore_hw_04/dz6_1/salaries.txt
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума зп: {total}, Середня зп: {average}")
