import matplotlib.pyplot as plt
import numpy

def my_solution(A):
    #print("my_solution - start")
    p = []
    p.insert(0, 0)
    
    #start_idxs = []
    #start_idxs.append(0)
    #avg = numpy.mean(A)
    for idex in range(len(A)):
        p.insert(idex + 1, p[idex] + A[idex])
        #if idex > 0 and (p[idex+1] < p[idex] or A[idex] < A[idex - 1]):  #and A[idex] <= avg:
            #start_idxs.append(idex - 1)
            #start_idxs.append(idex)
    
    #start_idxs = list(set(start_idxs))
    #start_idxs.sort() 
    
    #print("len A: {} - len start_idxs: {}".format(len(A), len(start_idxs)))
    #print(start_idxs)
    smallest_avg = None
    result_idx = 0
    #calculate_max_2_idx = False
    for start_idx in range(len(A)-1):
        for end_idx in range(start_idx + 1, len(A)):
            current_avg = (p[end_idx + 1] - p[start_idx]) / (end_idx - start_idx + 1)
            if None == smallest_avg:  
                smallest_avg = current_avg
                result_idx = start_idx
            elif current_avg < smallest_avg:
                smallest_avg = current_avg
                result_idx = start_idx
                #print("start_idx: {} - end_idx: {}".format(start_idx, end_idx))
            if (end_idx - start_idx) > 2:
                #After doing statistics, I observe the result will have start and end idex apart not more than 2 idex
                #Therefore, if it spreads more than 2 indexs, it's not worth to calculate anymore.
                break
            
        #if 2 >= (end_idx - start_idx):
        #This is the point where things get concentrate
            #calculate_max_2_idx = True
    
    print("my_solution - end")
    return result_idx

def standard_solution(A,plot=False):
    p = []
    p.insert(0, 0)
    
    for idex in range(len(A)):
        p.insert(idex + 1, p[idex] + A[idex])
        #print(p[idex + 1])
    avg = [[0 for x in range(len(A))] for x in range(len(A)-1)]
    smallest_idex = 0
    smallest_avg = None
    for idex in range(len(A)-1):
        for idex2 in range(idex+1,len(A)):
            avg[idex][idex2] = (p[idex2+1] - p[idex]) / (idex2 -idex + 1)
            if None == smallest_avg:
                smallest_avg = avg[idex][idex2]
            else:
                if avg[idex][idex2] < smallest_avg:
                    smallest_avg = avg[idex][idex2]
                    smallest_idex = idex
    if plot:                   
        #print(smallest_idex)
        """
        for idex in range(len(A) - 1):
            plt.plot(range(0, len(A)), avg[idex], 'o:')
        """
        
        plt.plot(range(len(A)), A, 'o:g')
        plt.plot(range(len(A)), avg[smallest_idex],'o:r')
        plt.plot(range(len(A) + 1), p, 'o--')
        plt.plot(smallest_idex,smallest_avg,'*')
            
        plt.show()
    
    return smallest_idex

def test(A=[10, 10, -1, 2, 4, -1, 2, -1], autogen = False, test_till_fail = False):
    while True:
        if autogen:
            A = numpy.random.uniform(-10000, 10000, 800)
            #A = numpy.array([0, 10])
        
        my_solution_idx = my_solution(A)
        standard_idx = standard_solution(A)
        print("=================")
        print(A)
        if standard_idx != my_solution_idx:
            print("[FAILED]: expected {}, got {}".format(standard_idx, my_solution_idx))
            standard_solution(A, plot = True)
            break
        else:
            print("[PASSED]: expected {}, got {}".format(standard_idx, my_solution_idx))
        print("=================")
        
        if not test_till_fail:
            break

test(autogen=True, test_till_fail=True)