f = None

for i in range(5):
    with open("data.txt", "w") as f:
        # if i & amp:
        # amp;gt; 2:
            break

print (f.closed)

##########################

# try:
#     if '1' != 1:
#         raise Exception("someError")
#     else:
#         print("someError has not occured")
# except "someError":
#     print ("someError has occured")


#==================================================

import numpy as np
a = np.array([1,2,3,4,5])
p = np.percentile(a, 10) #Returns 50th percentile, e.g. median
print(p)