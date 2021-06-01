#Convert a list of multiple integers into a single integer

L = [11, 33, 50]
print("Original integers: ",L)
print("Integer to List:: ", map(str,L))

x = int(''.join(map(str,L)))
print("Single integer:: ",x)

# convert number to list of integer
num = 113350
print([int(x) for x in str(num)])