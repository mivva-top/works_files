with open('input.txt', 'r+', encoding='utf-8') as f:
    NumStr = len(f.readlines())
    length = len('input.txt')
with open('statistics.txt', 'w+', encoding='utf-8') as f:
    f.write(str(NumStr))
    f.write('\n')
    f.write(str(length))
