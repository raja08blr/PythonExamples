st = "malyam"
# print(int(len(st)/2))
def pol_or_not(st):

    for i in range(0,int(len(st)/2)):
        if st[i] != st[int(len(st))-i-1]:
            return False
        return True
# print(pol_or_not("mayam"))
print(pol_or_not("malayalam"))