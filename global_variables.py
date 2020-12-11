def my_func():
    x = "local"
    print(x)

def my_func2():
    global x
    x = "changed"
    
x = "global"
    
my_func()

print(x)

my_func2()
print(x)