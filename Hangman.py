# Stage 5/8 of the Hangman project
import random

print("H A N G M A N\n")
answer = ('python', 'java', 'kotlin', 'javascript')

random_index = random.randint(0, 3)
random_answer = answer[random_index]
hidden_answer = list('-'*len(random_answer))

for i in range(8):
    print("".join(hidden_answer))
    letter = input("Input a letter:")

    if letter in random_answer:
        index = random_answer.find(letter)
        hidden_answer[index] = letter

    else:
        print("No such letter in the word")

    print()

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
