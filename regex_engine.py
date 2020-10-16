# regex engine project - stage 1/6

def single_char_comparasion(s):
    index = s.find('|')
    if index == 0 or index == -1:
        return True
    elif index == 1 and len(s) == 2:
        return False
    else:
        if s[0] == '.':
            return True
        if s[0] == s[2]:
            return True
        else:
            return False


print(single_char_comparasion(input("Input: ")))