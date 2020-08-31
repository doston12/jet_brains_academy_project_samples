# stage 2/5 of the Tic Tac Toe project

game = input("Enter cells: ")

print("---------")

for i in range(0, 9, 3):
    print('|', game[i], game[i+1], game[i+2], '|')

print("---------")

if game[0] == 'X' and game[1] == 'X' and game[2] == 'X' \
    or game[3] == 'X' and game[4] == 'X' and game[5] == 'X' \
    or game[6] == 'X' and game[7] == 'X' and game[8] == 'X' \
    or game[0] == 'X' and game[3] == 'X' and game[6] == 'X' \
    or game[1] == 'X' and game[4] == 'X' and game[7] == 'X' \
    or game[2] == 'X' and game[5] == 'X' and game[8] == 'X' \
    or game[0] == 'X' and game[5] == 'X' and game[8] == 'X' \
    or game[2] == 'X' and game[5] == 'X' and game[6] == 'X':
    print("X wins")
elif game[0] == 'O' and game[1] == 'O' and game[2] == 'O' \
    or game[3] == 'O' and game[4] == 'O' and game[5] == 'O' \
    or game[6] == 'O' and game[7] == 'O' and game[8] == 'O' \
    or game[0] == 'O' and game[3] == 'O' and game[6] == 'O' \
    or game[1] == 'O' and game[4] == 'O' and game[7] == 'O' \
    or game[2] == 'O' and game[5] == 'O' and game[8] == 'O' \
    or game[0] == 'O' and game[5] == 'O' and game[8] == 'O' \
    or game[2] == 'O' and game[5] == 'O' and game[6] == 'O':
    print("O wins")

if '-' in user_input:
    print("Game not finished")

"""
"""