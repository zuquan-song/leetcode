
def shift_strings(st, left, right):
    n = len(st)
    left, right = left % n, right % n
    st = st[left:] + st[:left]
    st = st[-right:] + st[:-right]
    return st

print(shift_strings('abcde', 2, 0))
print(shift_strings('abcde', 0, 2))
print(shift_strings('abcde', 2, 2))