file_name = "adressbook.txt"
def search_name(word, search):
    if search in word:
        return True

while True:
    print("Введите номер действия:\n1 - Показать все записи\n2 - Найти запись по вхождению частей имени\n3 - Найти запись по телефону\n4 - Добавить новый контакт\n5 - Удалить контакт\n6 - Изменить номер телефона у контакта\n7 - Выход\n**************")
    choice = int(input("Ввод: "))
    if choice == 1:
        print("**************")
        print("Все записи из адресной книги:")
        with open(file_name, "r", encoding="UTF-8") as f:
            for num, line in enumerate(f):
                print(num + 1, ". ", line.strip())
        print("**************")

    if choice == 2:
        print("**************")
        find = input("Введите часть имени, фамилии или отчества: ")
        print(f'\n"{find}" встречается в следующих записях:')
        with open(file_name, "r", encoding="UTF-8") as f:
            count = 0
            for number, line in enumerate(f):
                for word in line.split(", "):
                    if word.index != 3 and find in word:
                        print(number + 1, ". ", line.strip())
                        count +=1
                        break
            if count == 0:
                print("Записей удовлетворяющих условию не обнаружено")
        input("Для возврата в меню нажмити <Enter>")

        print("**************")
    
    if choice == 3:
        print("**************")
        find = input("Введите номер телефона: ")
        print(f'\n"Номер телефона: "{find}" встречается в следующих записях:')
        with open(file_name, "r", encoding="UTF-8") as f:
            count = 0
            for number, line in enumerate(f):
                print(line.strip().split(", ")[3])
                print(len(find))
                if find == line.strip().split(", ")[3]:
                    print(number + 1, ". ", line.strip())
                    count +=1
            if count == 0:
                print("Записей удовлетворяющих условию не обнаружено")
        input("Для возврата в меню нажмити <Enter>")

        print("**************")

    if choice == 4:
        name = input("Введите имя: ")
        patronim = input("Введите отчество: ")
        surname = input("Введите фамилию: ")
        phone = input("Введите номер телефона: ")
        contact = f'{surname}, {name}, {patronim}, {phone}\n'
        with open(file_name, "a", encoding="UTF-8") as f:
            f.write(contact)
        print("Данные успешно записаны")
        print("**************")

    if choice == 5:
        print("**************")
        address_book = []
        with open(file_name, "r", encoding="UTF-8") as f:
            for num, line in enumerate(f):
                print(num + 1, ". ", line.strip())
                address_book.append(line.strip())
        to_del = input("Введите номер контакта для удаления или 'q' для возврата в меню: ")
        if to_del != "q" and to_del.isdigit():
            to_del = int(to_del)
            print(f'Удален следующий контакт: {address_book.pop(to_del-1)}')
            with open(file_name, "w", encoding="UTF-8") as f:
                for el in address_book:
                    f.writelines(el+"\n")
        print("**************")

    if choice == 6:
        print("**************")
        address_book = []
        with open(file_name, "r", encoding="UTF-8") as f:
            for num, line in enumerate(f):
                print(num + 1, ". ", line.strip())
                address_book.append(line.strip())
        to_change = input("Введите номер контакта, у которой следует изменить телефон или 'q' для возврата в меню: ")
        new_phone = input("введите новый номер телефона: ")
        if to_change != "q" and to_change.isdigit():
            to_change = int(to_change)
            f,i,o,t = address_book.pop(to_change-1).split(", ")
            address_book.insert(to_change-1, f'{f}, {i}, {o}, {new_phone}')
            with open(file_name, "w", encoding="UTF-8") as f:
                for el in address_book:
                    f.writelines(el+"\n")
        print(f"Номер {t} успешно изменен на {new_phone}")
        print("**************")
    
    if choice == 7:
        print("До свидания")
        exit()
