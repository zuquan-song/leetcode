
def isTripleSquare(a, b, c):
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2

def tripleSquareSum(array):
    if len(array) < 3:
        return []
    n = len(array)
    res = []
    for i in range(n-2):
        if isTripleSquare(array[i], array[i+1], array[i+2]):
            res.append(1)
        else:
            res.append(0)
    return res

if __name__ == '__main__':
    print(tripleSquareSum([0,5,5,0,5,13,12]))