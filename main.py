cowbet = input()
word = input()

x = 0
letter = word[x]
unsolved = True
count = 0

while unsolved:
    count += 1
    for i in cowbet:
        if i == letter:
            x += 1
            try:
                letter = word[x]
            except:
                unsolved = False

print(count)
