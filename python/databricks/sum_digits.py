
def sum_digit(input1, input2):
    res = ""
    i = 0
    m, n = len(input1), len(input2)
    if m > n:
        m, n, input1, input2 = n, m, input2, input1

    while i < m:
        res += str(int(input1[i]) + int(input2[i]))
        i += 1

    while i < n:
        res += input2[i]
        i += 1

    return res

print(sum_digit("99", "99"))
print(sum_digit("29", "17"))
print(sum_digit("29", "177"))
print(sum_digit("177", "29"))