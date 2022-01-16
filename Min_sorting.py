"""two Python functions to find the minimum number on a list
The first utilizes O(n^2) and the second one, O(n) linear
 """
__author__= "Vaggelis Tikas"
import numpy as np
from random import randrange
import time

def square_min(item):
    overallmin = item[0]
    for i in item:
        issmallest = True
        for j in item:
            if i>j:
                issmallest =False
                min =j
        if issmallest:
            overallmin = i

    return overallmin

def lin_min(item,s=0):
    min=item[0]
    for i in item:
        if i<min:
            min = i

    return min

# listsize1 = input("Give the listsize:")
# blist=[]
# for i in blist:
#     blist[i]=input("Give the {} element".format(i))
#
# print(blist)

#print(square_min(blist))
#print(lin_min(blist))

"""
Compare the time between these algorithms
"""
print("Searching via O[n^2] function in python")
for listsize in range(1000,5001,1000):
    alist = [randrange(100000) for x in range(listsize)]

    start = time.time()
    print("Min: ",square_min(alist))
    end = time.time()
    print("size: %d time: %f"% (listsize, end - start))

print("Searching via O[n] function in python")
for listsize in range(1000,5001,1000):
    alist = [randrange(100000) for x in range(listsize)]
    start = time.time()
    print("Min: ",lin_min(alist))
    end = time.time()
    print("size: %d time: %f"% (listsize, end - start))