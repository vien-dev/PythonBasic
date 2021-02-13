def solution(S, P, Q):
    # write your code in Python 3.6
    # how many impacts of each type summed up at a specific position
    A = []
    C = []
    G = []

    index = 0
    A.insert(0,0)
    C.insert(0,0)
    G.insert(0,0)
    for nucleotide in S:
        A.insert(index + 1, A[index])
        C.insert(index + 1, C[index])
        G.insert(index + 1, G[index])
        if 'A' == nucleotide:
            A[index + 1] += 1
        elif 'C' == nucleotide:
            C[index + 1] += 1
        elif 'G' == nucleotide:
            G[index + 1] += 1
        index += 1
    
    result = []
    for index in range(len(P)):
        # We need to plus one because the prefix sum has first ele as 0
        # however, for the start index we don't +1 because we include the start index
        start_index = P[index]
        end_index = Q[index] + 1
        if (A[end_index] - A[start_index]) > 0:
            result.insert(index,1)
        elif (C[end_index] - C[start_index]) > 0:
            result.insert(index,2)
        elif (G[end_index] - G[start_index]) > 0:
            result.insert(index,3)
        else:
            result.insert(index,4)

    return result

S = 'CAGTAGT'
P = [2,0,2,2,1]
Q = [2,len(S) - 1,3,4,3]

result = solution(S,P,Q)
print(result)