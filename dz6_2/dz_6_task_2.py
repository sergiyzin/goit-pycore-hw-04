# Функція читає файлик з котами і повертає список словників
def get_cats_info(path: str) -> list[dict]:
    cats = []  # збирати котів

    try:
        # відкриваємо файл через with, щоб він сам і закрився
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # якщо порожній рядок, то пропускаєио
                if not line:
                    continue

                try:
                    # рядок у форматі: "id,name,age"
                    cat_id, name, age = line.split(",")
                except ValueError:
                    # якщо формат кривий, тобто, не 3 елементи як у нас, то пропускаємо
                    continue

                # формуємо словник з потрібними нам ключами
                cat_data = {
                    "id": cat_id,
                    "name": name,
                    "age": age,
                }

                # додаємо словник у список котів
                cats.append(cat_data)

        # повертаємо список котів
        return cats

    except FileNotFoundError:
        # якщо файл не знайдено, то повертаємо порожній список
        return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
