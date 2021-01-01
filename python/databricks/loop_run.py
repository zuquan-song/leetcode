
def loop_run(input):
    n = len(input)

    result = 0
    while any([val != 0 for val in input]):
        i = 0
        while i < n and input[i] == 0:
            i += 1

        x = input[i]
        while i < n and input[i] >= x:
            input[i] -= x
            i += 1
        result += x
        print(input)
    return result

# print(loop_run([5,1,3,4,5]))
# print(loop_run([1,7,2,3,6,9,1,7,8,5,1,9,2,87,3,561,92837,56129,8375,612]))