from pathlib import Path
file_path = Path("C:/Users/frygo/PycharmProjects/files/venv/labka.txt")
if file_path.exists():
    with open(file_path, encoding="utf-8") as file:
        lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        word_count = len(line.split())
        print(f"Строка {i}: Количество слов: {word_count}, Количество символов: {len(line)}")
else:
    print("Файл не существует.")
