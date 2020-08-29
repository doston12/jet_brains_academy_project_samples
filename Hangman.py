# Stage 2/8 of the Hangman project

print("H A N G M A N")
answer = "python"

word = input("Guess the word: ")

if answer == word:
    print("You survived!")
else:
    print("You are hanged!")