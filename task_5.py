with open('Resourse/words.txt', 'r+', encoding='utf-8') as f:
    words = [line.strip() for line in f if line.strip()]

sorted_alpha = sorted(words)
sorted_by_len = sorted(words, key=len)
sorted_reverse = sorted(words, reverse=True)

with open('sorted_alphabetically.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted_alpha))

with open('sorted_by_length.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted_by_len))

with open('sorted_reverse.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted_reverse))

print("Слова отсортированы и сохранены:")
print("- sorted_alphabetically.txt (по алфавиту)")
print("- sorted_by_length.txt (по длине)")
print("- sorted_reverse.txt (обратный алфавит)")
