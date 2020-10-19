# write your code here
import sys
sys.setrecursionlimit(10000)

def check_regex(re, ch):
    return True if re == '' or re == '.' or re == ch else False

def check_whole(regex, word):
    if not regex:
        return True
    elif not word:
        return False
    elif len(word) == 1:
        return check_regex(regex, word)
    elif check_regex(regex[0], word[0]):
        return check_whole(regex[1:], word[1:])
    else:
        return False

def check_sub(regex, word):
    if len(regex) > len(word):
        return False
    else:
        temp = True
        for i in range(0, len(regex)):
            if regex[i] != '.' and regex[i] != word[i]:
                temp = False
                break
        if not temp:
            return check_sub(regex, word[1:])
        else:
            return temp

regex, word = input().split('|')
print(check_sub(regex, word))