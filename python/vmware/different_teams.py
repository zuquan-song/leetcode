import collections

def different_teams(skills):
    counter = collections.Counter(skills)
    return min(counter.values())

print(different_teams('pcmbzpcmbz'))
print(different_teams('pcmbzpcmbzpcm'))
