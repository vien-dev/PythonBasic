class MyNumber():
    def __init__(self):
        self.a = 1
        
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if (self.a <= 3):
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
    def __getsource__(self):
        print("return a serie of number from 1 to 3")

mn = MyNumber()

try:
    for nu in mn:
        print(nu)
    else:
        print("It's the end of the loop")
        print("the for loop is stopped by StopInteration in the next")
        print("It already consumed that and comes to this else")
        print("If we want to handle StopIteration for the try, we need to raise another StopIteration")
        raise StopIteration
except StopIteration:
    print("End of my numbers")
    
    
del mn

mn = MyNumber()

iterable = iter(mn)

try: 
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))
except:
    print("End of my numbers")
    import traceback as tb
    import sys
    t, v, trb = sys.exc_info()
    tb.print_tb(trb)