def solution(A, K):
    size = len(A)
    offset = K % size
    B = []
    if 0 == offset:
        B =  A
    else:
        for index in range(size):
            #Python supports negative index
            B.insert(index, A[index - offset] )
    return B

A = [1, 3, 5, 7, 9, 2]
K = 6
S = solution(A, K)

print(S)