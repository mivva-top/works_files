print("Сортировка слов")

try:
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file.readlines()]

    words = [word for word in words if word]

    print(f" Файл words.txt прочитан")
    print(f"  Найдено слов: {len(words)}")

    if not words:
        print("  Файл пуст или не содержит слов!")
        exit()

    print("\nПервые 5 слов из файла:")
    for i, word in enumerate(words[:5], 1):
        print(f"  {i}. {word}")

    sorted_alpha = sorted(words)

    with open('sorted_alphabetically.txt', 'w', encoding='utf-8') as file:
        for word in sorted_alpha:
            file.write(word + '\n')

    print("\n Сортировка по алфавиту (A-Z) сохранена в sorted_alphabetically.txt")

    sorted_by_length = sorted(words, key=len)

    with open('sorted_by_length.txt', 'w', encoding='utf-8') as file:
        for word in sorted_by_length:
            file.write(word + '\n')

    print(" Сортировка по длине сохранена в sorted_by_length.txt")

    sorted_reverse = sorted(words, reverse=True)

    with open('sorted_reverse.txt', 'w', encoding='utf-8') as file:
        for word in sorted_reverse:
            file.write(word + '\n')

    print(" Сортировка в обратном порядке (Z-A) сохранена в sorted_reverse.txt")

    print("Примеры сортировки (первые 5 слов):")

    print("\nПо алфавиту (A-Z):")
    for i, word in enumerate(sorted_alpha[:5], 1):
        print(f"  {i}. {word}")

    print("\nПо длине (от коротких к длинным):")
    for i, word in enumerate(sorted_by_length[:5], 1):
        print(f"  {i}. {word} (длина: {len(word)})")

    print("\nВ обратном порядке (Z-A):")
    for i, word in enumerate(sorted_reverse[:5], 1):
        print(f"  {i}. {word}")

    print("Статистика:")

    shortest = sorted_by_length[0]
    longest = sorted_by_length[-1]
    print(f"Самое короткое слово: '{shortest}' (длина: {len(shortest)})")
    print(f"Самое длинное слово: '{longest}' (длина: {len(longest)})")

    avg_length = sum(len(word) for word in words) / len(words)
    print(f"Средняя длина слова: {avg_length:.1f} символов")

except FileNotFoundError:
    print(" Ошибка: Файл words.txt не найден!")
    print("  Создайте файл words.txt со словами (каждое слово на новой строке)")
except Exception as e:
    print(f" Ошибка: {e}")