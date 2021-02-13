def solution(A):
    current_sum = 0
    best_sum = float('-inf')
    for a in A:
        current_sum = max(a, current_sum + a)
        best_sum = max(best_sum, current_sum)
        #print("current sum: {} - best sum: {}".format(current_sum, best_sum))
    
    return best_sum

def solution_with_indices(A):
    current_sum = 0
    best_sum = float('-inf')
    candiate_start_index = end_index = 0
    for idx in range(len(A)):
        if (A[idx] > current_sum + A[idx]):
            current_sum = A[idx]
            candiate_start_index = idx
        else:
            current_sum += A[idx]
        
        if (current_sum > best_sum):
            best_sum = current_sum
            start_index = candiate_start_index
            end_index = idx
        
        print("current sum: {}, best sum: {}. start idx: {} - end idx: {}".\
              format(current_sum, best_sum, start_index, end_index))
    
    return (best_sum, start_index, end_index)
            

import generator as g

#A = g.generate(-200, 200, 8)
#A = [-155, 103, 99, -179, -69, 55, -191, -103]
#A = (-1,-2,-3,-4)
#A = (1, 2, 3, 4)
#A = (1, -2, 3, 4)
print(A)
print(solution(A))
print(solution_with_indices(A))