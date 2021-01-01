

def switch_integer(value):
    vstr = str(value)
    n = len(vstr)
    res = ""
    for i in range(0, n, 2):
        if i < n - 1:
            res += vstr[i+1] + vstr[i]
        else:
            res += vstr[i]
    return int(res)

print(switch_integer(12345))