l = [-2, -22, 10, 1, 11, -8, 0]

for j in range(len(l)):
    i = 0
    while i < len(l) - 1:
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
        i = i + 1
print(l)


def sort_without_built_in_func():
    l = [-2, -22, 10, 1, 11, -8, 0]
    for j in range(len(l)):
        i = 0
        while i<len(l)-1:
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
            i = i + 1
    print(l)


sort_without_built_in_func()
