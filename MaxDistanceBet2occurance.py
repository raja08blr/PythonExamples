lis = [1,2,0,3,4,2,8,2,3]
n = 2
sum = 5
emp_lis=[]
for i in range(len(lis)):
    if (lis[i])==n:
        emp_lis.append(i)
# print(emp_lis)
# print("Max dis",emp_lis[-1]-emp_lis[0])

#####################

# for j in range(len(lis)):
# i = 0
# while i < len(lis) - 1:
#     if (lis[i]+lis[i+1])==10:
#         print(i,i+1)
#         # break
#     i=i+1
for j in range(0,len(lis)-1):
    if (lis[j]+lis[j+1])==10:
        print(j,j+1)
