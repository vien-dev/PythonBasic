def standard_solution(A):
    class Point():
        def __init__(self, idx):
            self.index = idx
            self.is_end_point = False
        
        def set_point(self, point):
            self.point = point
        def set_is_end_point(self):
            self.is_end_point = True
        def get_point(self):
            return self.point
        def get_is_end_point(self):
            return self.is_end_point
        def get_index(self):
            return self.index
        
    points = []
    for idx in range(len(A)):
        point = Point(idx)
        point.set_point(idx - A[idx])
        points.append(point)
        point = Point(idx)
        point.set_point(idx + A[idx])
        point.set_is_end_point()
        points.append(point)

    """
    for circle in circles:
        print("{}: {}".format(circle.get_index(), circle.get_point()))
    """
    points.sort(key=lambda point: point.get_point())
    """
    for point in points:
        print("{}: {}".format(point.get_index(), point.get_point()))
    """
    
    total_intersection = 0
    for loop_idx in range(len(points)):
        if not points[loop_idx].get_is_end_point():
            start_idx = points[loop_idx].get_index()
            #print("===== start idx: {} =========".format(start_idx))
            if loop_idx > 0:
                for idx in range(loop_idx - 1, 0, -1):
                    if points[idx].get_point() == points[loop_idx].get_point() \
                        and points[idx].get_is_end_point():
                        #print(points[idx].get_index())
                        total_intersection += 1
            for idx in range(loop_idx+1, len(points)):
                if points[idx].get_is_end_point() and points[idx].get_index() != start_idx:
                    #print(points[idx].get_index())
                    total_intersection += 1
                elif points[idx].get_index() == start_idx:
                    #That's the end of the current concerned circle, break
                    break
            
            if total_intersection > 10000000:
                total_intersection = -1
                break
    
    return total_intersection

def solution(A):
    class Point():
        def __init__(self, is_starting_point=False):
            self.starting_point = is_starting_point
        
        def set_point(self, point):
            self.point = point
 
        def get_point(self):
            return self.point
        
        def is_starting_point(self):
            return self.starting_point
    
    points = []
    for idx in range(len(A)):
        start_point = Point(True)
        start_point.set_point(idx - A[idx])
        points.append(start_point)
        end_point = Point()
        end_point.set_point(idx + A[idx])
        points.append(end_point)

    points.sort(key=lambda point: point.get_point())
    """
    for point in points:
        print("{} - Start point: {}".format(point.get_point(), point.is_starting_point()))
    """
        
    """
    This solution bases on the idea that each circle at a particular start point 
    will be wrapped by circles that starts but not ends (or ends at the same start point)
    Therefore:
    1. Whenever reach a start point: total disc intersection += active circles before this point
       Then active circles += 1
    2. When reach an end point:
    """
    active_circles_before_me = 0
    total_disc_intersection = 0
    end_point = None
    continuos_end_point = 0
    for point in points:
        #print("{} - Start point: {}".format(point.get_point(), point.is_starting_point()))
        if end_point != None and end_point.get_point() != point.get_point():
            active_circles_before_me -= continuos_end_point
            end_point = None
            continuos_end_point = 0
            
        #print(active_circles_before_me)
        if point.is_starting_point():
            total_disc_intersection += active_circles_before_me
            #plus 1 for myself
            active_circles_before_me += 1
        else:
            #we still count the boundary as a part of the circle
            #therefore, don't decrease the active circles until it really passes the circle's boundary
            end_point = point
            continuos_end_point += 1
            continue
                  
        #print(total_disc_intersection)
        if total_disc_intersection > 10000000:
            total_disc_intersection = -1
            break
    
    return total_disc_intersection

#A = [1,5,2,1,4,0]
#A = [1, 0, 1, 0, 1]
#A=[1,0,1]
#A=[5,4,3]
#A=[0,0,1]
A=[0,1,0]
print(solution(A))

"""
continue_testing = True
test_per_bunch = 1000
element_count = 2
while continue_testing:
    import generator
    A = generator.generate(0, 200, element_count)
    print(A)
    std_solution = standard_solution(A)
    sol = solution(A)

    if std_solution != sol:
        print("[FAILED] expected: {} - got: {}".format(std_solution, sol))
        continue_testing = False
    else:
        print("[PASSED] expected: {} - got: {}".format(std_solution, sol))
    
    test_per_bunch -= 1
    if 0 == test_per_bunch and element_count <= 5000:
        element_count += 1
        test_per_bunch = 1000
"""
