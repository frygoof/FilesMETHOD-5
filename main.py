file_name = "labka.txt"
with open(file_name, "w", encoding="utf-8") as file:
    while True:
        user_input = input("Введите данные (пустая строка для завершения): ")
        if user_input == "":
            break
        file.write(user_input + "\n")
print("Текстовый файл обновлен:", file_name)