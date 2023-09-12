from utils import search_and_correct_operations, reverse_and_show_5_operations_list


start = input(print(f"Пожалуйста, введите номер комманды. "
                    f"1. Показать счет. "
                    f"2. Показать последние 5 успешных операций. "))

if start == "1":
    print("Данный функционал пока не рабоатет, нажмите другую кнопку. ")

if start == "2":
    operations_list = reverse_and_show_5_operations_list()

    for operations in operations_list:
        card = operations["from"]
        card_number = card.split()[-1]
        card_name_bank = card.split()[0]

        private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        chunks, chunk_size = len(private_number), len(private_number) // 4
        show_cart = " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])

        bank_account = operations["to"]
        account_numb = bank_account.split()[-1]
        name_account = bank_account.split()[0]

        show_account = "**" + account_numb[-4:]

        print(f'{operations["date"]} {operations["description"]}')
        print(f'{card_name_bank} {show_cart} -> {name_account} {show_account}')
        print(f'{operations["operationAmount"]["amount"]} {operations["operationAmount"]["currency"]["name"]}')
        print()
