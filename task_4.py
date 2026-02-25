SHIFT = 3

print("Шифр Цезаря")

try:
    with open('secret.txt', 'r', encoding='utf-8') as f:
        original = f.read()

    print(f" Файл secret.txt прочитан ({len(original)} символов)")

    encrypted = ""
    for char in original:
        if 'а' <= char <= 'я':
            new_pos = (ord(char) - ord('а') + SHIFT) % 32
            encrypted += chr(ord('а') + new_pos)
        elif 'А' <= char <= 'Я':
            new_pos = (ord(char) - ord('А') + SHIFT) % 32
            encrypted += chr(ord('А') + new_pos)
        elif 'a' <= char <= 'z':
            new_pos = (ord(char) - ord('a') + SHIFT) % 26
            encrypted += chr(ord('a') + new_pos)
        elif 'A' <= char <= 'Z':
            new_pos = (ord(char) - ord('A') + SHIFT) % 26
            encrypted += chr(ord('A') + new_pos)
        else:
            encrypted += char

    with open('encrypted.txt', 'w', encoding='utf-8') as f:
        f.write(encrypted)

    print(" Текст зашифрован в encrypted.txt")

    decrypted = ""
    for char in encrypted:
        if 'а' <= char <= 'я':
            new_pos = (ord(char) - ord('а') - SHIFT) % 32
            decrypted += chr(ord('а') + new_pos)
        elif 'А' <= char <= 'Я':
            new_pos = (ord(char) - ord('А') - SHIFT) % 32
            decrypted += chr(ord('А') + new_pos)
        elif 'a' <= char <= 'z':
            new_pos = (ord(char) - ord('a') - SHIFT) % 26
            decrypted += chr(ord('a') + new_pos)
        elif 'A' <= char <= 'Z':
            new_pos = (ord(char) - ord('A') - SHIFT) % 26
            decrypted += chr(ord('A') + new_pos)
        else:
            decrypted += char

    with open('decrypted.txt', 'w', encoding='utf-8') as f:
        f.write(decrypted)

    print(" Текст расшифрован в decrypted.txt")

    if decrypted == original:
        print("\n Успех: Расшифрованный текст совпадает с оригиналом!")
    else:
        print("\n Ошибка: Расшифрованный текст отличается от оригинала!")

        print("\nПервые 50 символов:")
        print(f"Оригинал:  {original[:50]}")
        print(f"Расшифр.:  {decrypted[:50]}")

except FileNotFoundError:
    print(" Ошибка: Файл secret.txt не найден!")
except Exception as e:
    print(f" Ошибка: {e}")