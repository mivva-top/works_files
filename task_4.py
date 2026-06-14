def encrypt(text):
    result = ""
    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            if char.islower():
                result += chr((ord(char) - ord('а') + 3) % 32 + ord('а'))
            else:
                result += chr((ord(char) - ord('А') + 3) % 32 + ord('А'))
        elif char == 'ё':
            result += 'й'
        elif char == 'Ё':
            result += 'Й'
        else:
            result += char
    return result

def decrypt(text):
    result = ""
    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            if char.islower():
                result += chr((ord(char) - ord('а') - 3) % 32 + ord('а'))
            else:
                result += chr((ord(char) - ord('А') - 3) % 32 + ord('А'))
        elif char == 'й':
            result += 'ё'
        elif char == 'Й':
            result += 'Ё'
        else:
            result += char
    return result

print("1. Зашифровать (secret.txt -> encrypted.txt)")
print("2. Расшифровать (encrypted.txt -> decrypted.txt)")
choice = input("Выберите действие (1 или 2): ")

if choice == '1':
    with open('Resourse/secret.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    result = encrypt(text)
    with open('encrypted.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    print("Текст зашифрован и сохранен в encrypted.txt")

elif choice == '2':
    with open('encrypted.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    result = decrypt(text)
    with open('decrypted.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    print("Текст расшифрован и сохранен в decrypted.txt")

else:
    print("Неверный выбор!")
