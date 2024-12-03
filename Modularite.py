def modularite(A):
    q = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    d = [0 for i in range(len(A))]

    a_xx = 0

    for i in range(len(A)):
        for j in range(len(A[0])):
            d[i] += A[i][j]
            a_xx += A[i][j]

    for i in range(len(A)):
        for j in range(len(A[0])):
            q[i][j] = A[i][j] - ((d[i]*d[j])/a_xx)
    return q
