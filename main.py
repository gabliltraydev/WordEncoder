import random

i = 0

while i<26:
    rand = random.randint(1, 9999)
    print(rand)
    randStr = str(rand)
    with open(str(i) + '.txt', 'w') as file:
        file.write(randStr)
    i = i+1



