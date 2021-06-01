# l = [3,4,5,6,5,7]
l = [3,4,7,6,2,8,1,9,7]
l1=list(set(l))
k=10
out = []
for i in l1:
    diff = (k-i)
    if diff in l:
        l1.remove(diff)
        print("after pop",l1)
        out.append((i,diff))
print(out)