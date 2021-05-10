# find the pair in array whose sum is closest to x

MAX_VAL = 1000000000
def printClosest(arr,n,x):
    res_l,res_r=0,0
    # l,r,diff=0,n-1,MAX_VAL
    l=0
    r=n-1
    diff = MAX_VAL

    while r>l:
        if abs(arr[l]+arr[r]-x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l]+arr[r]-x)
        if arr[l]+arr[r]>x:
            r= r-1
            print(r)
        else:
            l=l+1
            print("l",l)
    print('The closest pair is {} and {}' .format(arr[res_l], arr[res_r]))
    # print('The closest pair is {} and {}' .format(arr[l], arr[r]))

# Driver code to test above
if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    n = len(arr)
    x=33
    printClosest(arr, n, x)

