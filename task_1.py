try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    line_count = len(lines)

    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)

    with open('statistics.txt', 'w', encoding='utf-8') as file:
        file.write(f"Количество строк: {line_count}\n")
        file.write(f"Количество слов: {word_count}\n")

    print(f"Статистика успешно записана в файл statistics.txt")
    print(f"Найдено строк: {line_count}")
    print(f"Найдено слов: {word_count}")

except FileNotFoundError:
    print("Ошибка: Файл input.txt не найден")
except Exception as e:
    print(f"Произошла ошибка: {e}")