# Stage 4/8 of the Hangman project
import random

print("H A N G M A N")
answer = ('python', 'java', 'kotlin', 'javascript')

random_index = random.randint(0, 3)
random_answer = answer[random_index]
x = random_answer[:3] + '-'*(len(random_answer)-3)
word = input(f"Guess the word: {x}")

if answer[random_index] == word:
    print("You survived!")
else:
    print("You are hanged!")