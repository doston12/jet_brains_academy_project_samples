# Stage 8/8 of the Hangman project
import random

print("H A N G M A N")

while True:

    player_action = input('Type "play" to play the game, "exit" to quit: ')

    if player_action == "play":

        player_lives = 8
        answer = ('python', 'java', 'kotlin', 'javascript')
        player_letters = []
        random_index = random.randint(0, 3)
        random_answer = answer[random_index]
        hidden_answer = list('-' * len(random_answer))

        while player_lives > 0:
            print()
            print("".join(hidden_answer))
            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("You should input a single letter")
                continue

            if not(ord(letter) >= 97 and ord(letter) <= 122):
                print("It is not an ASCII lowercase letter")

            else:

                if letter in player_letters:
                    print("You already typed this letter")

                else:

                    player_letters.append(letter)

                    if letter in random_answer:
                        indexes = []
                        for char_index in range(len(random_answer)):
                            if letter == random_answer[char_index]:
                                indexes.append(char_index)

                        for index in indexes:
                            hidden_answer[index] = letter

                    else:
                        player_lives -= 1
                        print("No such letter in the word")

        if player_lives <= 0:
            print("You are hanged!")
        else:
            print("You survived!")
            print("You guessed the word!")

    else:
        break


