import random as rdm

def generate(min_val, max_val, N):
    A = []
    #print(N)
    for idx in range(N):
        no = rdm.randint(min_val, max_val)
        #print("{}: {}".format(idx, no))
        A.insert(idx, no)
        
    return A
