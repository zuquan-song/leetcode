

def counting_sort(A):
    n = len(A)
    B = ['N'] * n
    C = [0] * (max(A) + 1)

    for i in range(n):
        C[A[i]] += 1

    for i in range(1, max(A) + 1):
        C[i] = C[i-1] + C[i]

    for j in range(0, n):
        # for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
        print("B={}".format(B))
        print("C={}".format(C))

counting_sort([2,5,3,0,2,3,0,3])