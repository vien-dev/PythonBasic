x = lambda number: number * 2
my_sum = lambda a,b=1: a+b

print(x(3))
print(my_sum(2,3))
print(my_sum(2))

def my_func(n):
    return lambda a: a*n

my_doubler = my_func(2)
my_trippler = my_func(3)

print(my_doubler(11))
print(my_trippler(11))