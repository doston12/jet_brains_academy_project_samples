import random

winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

player_name = input("Enter your name: ")
print("Hello,", player_name)
player_options = input().split(",")
print("Okay, let's start")

player_ratings = open('ratings.txt', 'r')
player_score = 0

players_with_scores = player_ratings.readlines()
for x in players_with_scores:
    player, score = map(str, x.split(' '))
    if player_name == player:
        player_score = int(score)
        break

conditions = []
if len(player_options) == 1:
    conditions = ['rock', 'paper', 'scissors']
else:
    conditions = player_options

user_choice = ""
options_lenght = len(conditions)

while True:
    user_choice = input()
    index = random.randint(0, options_lenght-1)
    computer_choice = conditions[index]

    if user_choice in conditions:
        user_winning_cases = winning_cases.get(user_choice)

        if user_choice == computer_choice:
            print("There is a draw ({})".format(user_choice))
            player_score += 50
        elif computer_choice in user_winning_cases:
            print("Well done. The computer chose {} and failed".format(computer_choice))
            player_score += 100
        elif computer_choice not in user_winning_cases:
            print("Sorry, but the computer chose {}".format(computer_choice))

    elif user_choice == '!exit':
        print("Bye!")
        break
    elif user_choice == '!rating':
        print('Your rating:', player_score)
    else:
        print("Invalid input")