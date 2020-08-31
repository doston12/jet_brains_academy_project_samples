
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

# reading a name
name = input()

print(f'What a great name you have, {name}!')
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
one = int(input())
two = int(input())
three = int(input())

age = (one * 70 + two * 21 + three * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
number = int(input())
for i in range(number+1):
    print(i, "!")
print("Completed, have a nice day!")