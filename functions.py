def add_one(
    number:int = 1 # type: int
): # type: int 
    number += 1
    return number

x = '2'
x = add_one(2)
print(x)

func_ptr = add_one

print(func_ptr(5))