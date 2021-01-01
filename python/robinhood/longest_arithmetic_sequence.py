import bisect

def is_ac(seq):
    n = len(seq)
    for i in range(2, n):
        if seq[i] - seq[i-1] != seq[i-1] - seq[i-2]:
            return False
    return True


def longest_arithmetic_sequence(a, b):
    for v in b:
        pass
