
word = input()

mid_index = len(word) // 2
forward =  word[:mid_index+1]
backward = word[::-1]
backward = backward[:mid_index+1]

if forward == backward:
    print("Yes")
else:
    print("No")