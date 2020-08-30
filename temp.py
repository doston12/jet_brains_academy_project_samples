
def what_to_do(instructions):
    instructions.strip()
    if instructions.startswith('Simon says') or instructions.endswith('Simon says'):
        x = instructions.replace('Simon says', '')
        ans = " ".join(x.split())
        return f"I {ans}"
    else:
        return "I won't do it!"

print(what_to_do("make a wish Simon says"))
print(what_to_do("Simon says love it"))
print(what_to_do("live Simon says it "))
print(what_to_do("like Simon it says "))
print(what_to_do("go away"))