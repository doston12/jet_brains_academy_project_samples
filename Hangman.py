# Stage 3/8 of the Hangman project
import random

print("H A N G M A N")
answer = ('python', 'java', 'kotlin', 'javascript')

word = input("Guess the word: ")
random_index = random.randint(0, 3)

if answer[random_index] == word:
    print("You survived!")
else:
    print("You are hanged!")