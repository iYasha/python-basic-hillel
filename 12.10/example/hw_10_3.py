"""
Дан многомерный список в котором находится результат игры в крестики нолики,
выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.
"""

board = [
    ['x', 'o', 'x'],
    ['o', 'x', 'o'],
    ['o', 'x', 'x'],
]

winner = None

for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
        winner = board[i][0]
    if board[0][i] == board[1][i] == board[2][i]:
        winner = board[0][i]
if board[0][0] == board[1][1] == board[2][2]:
    winner = board[0][0]
if board[0][2] == board[1][1] == board[2][0]:
    winner = board[0][2]

if winner:
    print(f'Winner is {winner}')
else:
    print('Draw')
