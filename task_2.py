search_word = input("Введите слово для поиска: ")

try:
    file_path = 'resource/text.txt'

    file = open(file_path , 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    found = False
    count = 0
    found_lines = []

    for i in range(len(lines)):
        line = lines[i]
        words = line.split()

        for word in words:
            clean_word = word.strip('.,!?;:"()[]{}').lower()
            if clean_word == search_word.lower():
                count = count + 1
                found = True
                if (i + 1) not in found_lines:
                    found_lines.append(i + 1)

    print("Результаты поиска:")

    if found:
        print(f"Слово '{search_word}' найдено в файле")
        print(f"Количество вхождений: {count}")
        print(f"Встречается в строках: {found_lines}")
    else:
        print(f"Слово '{search_word}' не найдено в файле")

    result_file = open('resource/search_results.txt', 'w', encoding='utf-8')
    result_file.write("Результаты поиска слова:\n")
    result_file.write(f"Искомое слово: {search_word}\n\n")

    if found:
        result_file.write(f"Статус: найдено\n")
        result_file.write(f"Количество вхождений: {count}\n")
        result_file.write(f"Номера строк: {found_lines}\n\n")
        result_file.write("Детали по строкам:\n")

        for line_num in found_lines:
            result_file.write(f"Строка {line_num}: {lines[line_num - 1].strip()}\n")
    else:
        result_file.write(f"Не найдено\n")

    result_file.close()

    print(f"Результаты также сохранены в файл search_results.txt")

except FileNotFoundError:
    print("Ошибка: Файл text.txt не найден")
except Exception as e:
    print(f"Произошла ошибка: {e}")