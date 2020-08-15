from functools import reduce

def team_formation(skills, k, l, r):
    counter = 0
    for skill in skills:
        if l <= skill <= r:
            counter += 1

    res = 0
    for players in range(k, counter+1):
        # eg. players=3, counter=5 => res += 5*4*3/3*2*1
        denominator = reduce(lambda x, y: x*y, range(1, players+1))
        numerator = reduce(lambda x, y: x*y, range(counter-players+1, counter+1))
        res += int(numerator/denominator)
    return res

print(team_formation([12,4,6,13,5,10], 3, 4, 10))

