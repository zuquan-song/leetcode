

def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))
    pos = len(product) - 1

    for n1 in reversed(num1):
        tmpPos = pos
        for n2 in reversed(num2):
            product[tmpPos] += int(n1) * int(n2)
            product[tmpPos - 1] += product[tmpPos] // 10
            product[tmpPos] = product[tmpPos] % 10
            tmpPos -= 1
        pos -= 1

    pt = 0
    while pt < len(product) - 1 and product[pt] == 0:
        pt += 1
    return "".join(map(str, product[pt:]))

if __name__ == '__main__':
    print(multiply("1234567890", "1234567890"))
    print(1234567890 * 1234567890)
