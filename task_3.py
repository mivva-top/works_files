files = ['file1.txt', 'file2.txt', 'file3.txt']

with open('combined.txt', 'w', encoding='utf-8') as outfile:
    for filename in files:
        try:
            with open(filename, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(f" Содержимое {filename} \n")
                outfile.write(content)
                outfile.write("\n\n")
        except FileNotFoundError:
            outfile.write(f" Содержимое {filename} \n")
            outfile.write(f"[Файл {filename} не найден]\n\n")

print("Файлы объединены в combined.txt")
