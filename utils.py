import json


with open('operations.json', 'r', encoding='utf-8') as file:
    operations = json.load(file)


def search_and_correct_operations():  # Функция для фильтрации правильных операций и корректировке даты
    operations_list = []

    for operation in operations:
        if operation == {}:
            continue
        if operation["state"] == "CANCELED":
            continue
        if operation["description"] == "Открытие вклада":
            continue
        else:
            operations_list.append(operation)
            format_date = f'{operation["date"][8:10]}-{operation["date"][5:7]}-{operation["date"][0:4]}'
            operation["date"] = format_date

    return sorted(operations_list, key=lambda k, reverse=True: '-'.join(reversed(k["date"].split('-'))))


def reverse_and_show_5_operations_list():  # Корректировка всего списка в правильном порядке и возвращает 5 последних операций
    operations_list = search_and_correct_operations()
    reverse_operations_list = operations_list[::-1]

    return reverse_operations_list[:5]

