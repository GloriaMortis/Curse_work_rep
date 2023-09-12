import json


with open('operations.json', 'r', encoding='utf-8') as file:
    operations = json.load(file)


def search_true_operations():  # Функция для фильтрации правильных операций
    operations_list = []

    for operation in operations:
        if operation == {}:
            continue
        if operation["state"] == "CANCELED":
            continue
        else:
            operations_list.append(operation)

    return operations_list


def format_date_for_search():  # Функция для корректировки времени

    operations_list = search_true_operations()

    for operation in operations_list:
        format_date = f'{operation["date"][8:10]}-{operation["date"][5:7]}-{operation["date"][0:4]}'

        operation["date"] = format_date
    return operations_list


def sorted_operations_list():  # Функция для сортировки списка

    operations_list = format_date_for_search()

    return sorted(operations_list, key=lambda k, reverse=True: '-'.join(reversed(k["date"].split('-'))))


def reverse_the_operations_list():  # Корректировка всего списка в правильном порядке
    operations_list = sorted_operations_list()
    reverse_operations_list = operations_list[::-1]

    return reverse_operations_list
