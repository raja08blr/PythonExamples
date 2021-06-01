# n(0)
def getMissingNum(a):
    n = len(a)
    total = ((n+1)*(n+2)/2)
    sum_a = sum(a)
    return total-sum_a
a=[1,2,4,5,6]
print(getMissingNum(a))