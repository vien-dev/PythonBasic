def solution(A):
	l2r_move = []
	l2r_move.append(0) #0
	l2r_move.append(0) #1
	current_max = 0
	for idx in range(2, len(A) - 1):
		#current_max = max(A[idx - 1], current_max + A[idx - 1])
		#print(current_max + A[idx - 1])
		current_max = max(0, current_max + A[idx - 1])
		l2r_move.append(current_max)	
	l2r_move.append(0) #len(A) - 1
	print(l2r_move)
	
	r2l_move = []
	r2l_move.append(0) #len(A) - 1
	r2l_move.append(0) #len(A) - 2
	current_max = 0
	for idx in range(len(A) - 3, 0, -1):
		#current_max = max(A[idx + 1], current_max + A[idx + 1])
		current_max = max(0, current_max + A[idx + 1])
		r2l_move.append(current_max)
	r2l_move.append(0) #0
	print(r2l_move)
	r2l_move.reverse()
	print(r2l_move)
	
	max_sum = float('-inf')
	for idx in range(1, len(A) - 1):
		max_sum = max(max_sum, l2r_move[idx] + r2l_move[idx])
		#print(max_sum)
	
	return max_sum
	

#A = [3,5,7]
#A = [3, 2, 6, -1, 4, 5, -1, 2]
A = [0, 10, -5, -2, 0]
#A = [-3,-5,-2,-1,-4]
print(A)
print(solution(A))
