import collections

def usernameSystem(names):
    counter = collections.defaultdict(int)
    res = []
    for name in names:
        res.append(name if counter[name] == 0 else name + str(counter[name]))
        counter[name] += 1
    return res

print(usernameSystem(['a', 'a', 'b', 'b']))