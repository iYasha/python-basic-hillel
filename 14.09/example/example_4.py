number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Поздравляю, вы угадали,')  # Начало нового блока
    print('(хотя и не выиграли никакого приза!)')  # Конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого.')  # Ещё один блок
    # Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
    # чтобы попасть сюда, guess должно быть больше, чем number
