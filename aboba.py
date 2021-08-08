count = 0
a = "aboba!"
while True:
    print(a)
    count += 1
    if count >= 100:
        print("Конец!")
        break
    choice = input("Хотите поменять слово?")
    if choice == "Да":
        name = input("Введите ваше слово: ")
        a = name
    else:
        continue