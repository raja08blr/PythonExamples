def canFormPalindrome(strr):
    listt=[]
    for i in range(len(strr)):
        if strr[i] in listt:
            listt.remove(strr[i])
            print(listt)
        else:
            listt.append(strr[i])
    # if character length is even
    # list is expected to be empty
    # or if character length is odd
    # listt size is expected to be 1
    if (len(strr) % 2 == 0 and len(listt) == 0 or
            (len(strr) % 2 == 1 and len(listt) == 1)):
        return True
    else:
        return False

# Driver code
if (canFormPalindrome("geeksforgeeks")):
    print("Yes")
else:
    print("No")

if (canFormPalindrome("GABBARR")):
    print("Yes")
else:
    print("No")

# This code is contributed by SHUBHAMSINGH10

