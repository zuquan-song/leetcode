
import collections

def swap_string(a: str, b: str):
    ca = [0] * 26
    cb = [0] * 26

    for ch in a: ca[ord(ch) - ord('a')] += 1
    for ch in b: cb[ord(ch) - ord('a')] += 1

    for i in range(26):
        if (ca[i] != 0 and cb[i] != 0) or (ca[i] == 0 and cb[i] == 0):
            pass
        else:
            return False

    ca = filter(lambda x: x != 0, ca)
    cb = filter(lambda x: x != 0, cb)
    return sorted(ca) == sorted(cb)


if __name__ == '__main__':
    print(swap_string('abbzccc', 'babzzcz'))
    print(swap_string('a', 'b'))