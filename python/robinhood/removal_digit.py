
def remove_digit(s, t):
    res = 0
    for i, ch in enumerate(s):
        if ch.isdigit() and s[:i]+s[i+1:] < t:
            print(s[:i]+s[i+1:], t)
            res += 1
    for i, ch in enumerate(t):
        if ch.isdigit() and s < t[:i]+t[i+1:]:
            print(s, t[:i]+t[i+1:])
            res += 1

    return res

if __name__ == '__main__':
    print(remove_digit('ab12c', '1zz456'))