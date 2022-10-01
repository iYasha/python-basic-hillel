
text = input("Enter text: ")
shift = int(input("Enter shift: "))

result = ''


for symbol in text:
    if symbol.islower():
        result += chr(ord('а') + (ord(symbol) - ord('а') + shift) % 32)
    elif symbol.isupper():
        result += chr(ord('А') + (ord(symbol) - ord('А') + shift) % 32)

print(result)

# for i in range(ord('А'), ord('А') + 33):
#     print(f'{i} = {chr(i)}')

