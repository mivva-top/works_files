word = input("Введите слово для поиска: ")

with open('Resourse/text.txt', 'r+', encoding='utf-8') as f:
    lines = f.readlines()

found_lines = []
total_count = 0

for i, line in enumerate(lines, 1):
    count = line.lower().count(word.lower())
    if count:
        found_lines.append(i)
        total_count += count

print(f"\nНайдено: {'Да' if found_lines else 'Нет'}")
print(f"Количество: {total_count}")
print(f"Строки: {', '.join(map(str, found_lines)) if found_lines else 'не найдено'}")

with open('search_results.txt', 'w', encoding='utf-8') as f:
    f.write(f"Слово: {word}\n")
    f.write(f"Найдено: {'Да' if found_lines else 'Нет'}\n")
    f.write(f"Количество: {total_count}\n")
    f.write(f"Строки: {', '.join(map(str, found_lines)) if found_lines else 'не найдено'}")
