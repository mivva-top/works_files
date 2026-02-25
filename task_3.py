input_files = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'combined.txt'

print("Объединение файлов")

existing_files = []
missing_files = []

for filename in input_files:
    file_path = 'resource/text.txt'

for filename in input_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_files.append(filename)
        print(f" {filename} - найден")
    except FileNotFoundError:
        missing_files.append(filename)
        print(f" {filename} - не найден")

if not existing_files:
    print(" Нет ни одного существующего файла для объединения!")
else:
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:

            for filename in existing_files:
                with open(filename, 'r', encoding='utf-8') as infile:
                    content = infile.read()

                outfile.write(f'=== Содержимое {filename} ===\n')

                if content:
                    outfile.write(content)
                else:
                    outfile.write('[файл пуст]')

                outfile.write('\n\n')

            if missing_files:
                outfile.write('=== Пропущенные файлы ===\n')
                for filename in missing_files:
                    outfile.write(f'- {filename} (не найден)\n')

        print(f"\n Файлы успешно объединены в {output_file}")
        print(f"   Объединено файлов: {len(existing_files)}")
        if missing_files:
            print(f"   Пропущено файлов: {len(missing_files)}")

    except Exception as e:
        print(f" Ошибка при записи: {e}")