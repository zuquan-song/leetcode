
def pattern_match(pattern, s):
    vowel = {'a', 'e', 'i', 'o', 'u'}
    n = len(s)
    sconv = "".join(['1' if ch in vowel else '0' for ch in s])
    m = len(pattern)
    counter = 0
    for i in range(n - m):
        if sconv[i: i+m] == pattern:
            counter += 1
    return counter


if __name__ == '__main__':
    print(pattern_match('010', 'amazing'))