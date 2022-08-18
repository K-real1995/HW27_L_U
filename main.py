from collections import Counter
import json
from pathlib import Path

# Первое задание
x = [1, 2, 3, 4, 2, 4, 5]


def mode(line: list):
    if not line:
        return []
    else:
        most_common = Counter(line).most_common()
        max_count = most_common[0][1]
        result = []
        for line, count in most_common:
            if count < max_count:
                break
            else:
                result.append(line)
        print(result)


mode(x)


# Второе задание


def get_data_in_db():
    with open('base.json') as f:
        data = json.load(f)
        return data["products"] if data["products"] else None


def make_data_in_db(title, quantity, cost):
    path = Path('base.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    # Data to be written
    dictionary = {
        "Название": title,
        "Количество": quantity,
        "Цена": cost
    }

    data['products'].append(dictionary)

    # Serializing json
    path.write_text(json.dumps(data), encoding='utf-8')


def main_func():
    while True:
        choice = int(input("___Меню___\n"
                           "1.Ввести данные\n"
                           "2 Вывести все введенные ранее данные\n"
                           "3.Выход\n"))
        if choice == 1:
            name = input("Введите название: ")
            count = int(input("Введите количество: "))
            price = int(input("Введите цену: "))
            make_data_in_db(name, count, price)
            print("Данные успешно добавлены")
        elif choice == 2:
            print(get_data_in_db())
        elif choice == 3:
            print("Выходим из программы")
            break  # Выход из цикла программы


main_func()


# Третье задание
def main_star():
    row = list(map(int, input().split(',')))
    counter = 0

    place = {}

    for i in range(0, len(row)):
        if row[i] == 0:
            counter += 1
        else:
            place[i - 1] = counter / 2
            counter = 0

    max_place = max(place, key=place.get)
    need_place = round(max_place - place.get(max_place) / 2)
    print("Самое удаленное место от других сидящих посетителей:", need_place)


main_star()
