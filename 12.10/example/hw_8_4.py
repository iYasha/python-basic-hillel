"""
Напишите программу где пользователь вводит число symbol_len, а программа генерирует пароль длинной symbol_len.
Чем выше будет сложность пароля, тем лучше.
"""

import random
import string

password_len = int(input('Give me password length: '))

password = ''
char_count = password_len // 4
rest_char = password_len % 4
all_symbols = string.ascii_letters + string.digits + string.punctuation
consistent_password = ''

for symbols in string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation:
    if char_count > len(symbols):
        consistent_password += ''.join(random.choices(symbols, k=char_count))
    else:
        consistent_password += ''.join(random.sample(symbols, k=char_count))

consistent_password += ''.join(random.choices(all_symbols, k=rest_char))

for _ in range(password_len):
    random_character = random.sample(consistent_password, k=1)[0]
    password += random_character
    consistent_password = consistent_password.replace(random_character, '', 1)

print(f'Your password: {password}')

