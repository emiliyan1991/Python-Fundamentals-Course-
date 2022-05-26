def phonebook():
    p_book = dict()
    info = input()
    while "-" in info:
        contact = info.split("-")
        name = contact[0]
        number = contact[1]
        p_book[name] = number
        info = input()
    n = int(info)

    for i in range(n):
        search_name = input()
        for key, value in p_book.items():
            if search_name == key:
                print(f"{key} -> {value}")
        if search_name not in p_book:
            print(f"Contact {search_name} does not exist.")

phonebook()

