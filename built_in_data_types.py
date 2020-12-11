x = b'Hello'
print(repr(x))

print((11).to_bytes(1, byteorder='big'))
x = pow(2,1000000)
print(x)
print(x.bit_length())

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

thisset = {'banana', 'apple', 'grape'}
thislist = ['abc', 'def']

thisset.update(thislist)
print(thisset)  

x = thisset.pop()
print(x)
thisset.clear()
print(thisset)
del thisset
#print(thisset)