# Stage 6/8 of the Hangman project
import random

print("H A N G M A N")
answer = ('python', 'java', 'kotlin', 'javascript')

player_lives = 8
player_letters = []
random_index = random.randint(0, 3)
random_answer = answer[random_index]
hidden_answer = list('-'*len(random_answer))

while player_lives > 0:
    print()

    print("".join(hidden_answer))
    letter = input("Input a letter: ")

    if letter in player_letters:
        print("No improvements")
        player_lives -= 1

    else:

        if letter in random_answer:
            indexes = []
            for char_index in range(len(random_answer)):
                if letter == random_answer[char_index]:
                    indexes.append(char_index)

            for index in indexes:
                hidden_answer[index] = letter
            player_letters.append(letter)

        else:
            player_lives -= 1
            print("No such letter in the word")

if player_lives <= 0:
    print("You are hanged!")
else:
    print("You survived!")
    print("You guessed the word!")

