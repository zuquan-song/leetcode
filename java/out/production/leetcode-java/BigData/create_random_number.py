import random

with open("random_number.txt", "w", buffering=10000) as output:
    i = 0
    lines = []
    while i < 10000000:
        i += 1
        lines.append(str(random.randint(0, 1000000)) + "\n")
        if i % 100000 == 0:
            output.writelines(lines)
            lines = []
