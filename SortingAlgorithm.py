'''Sorting Algorithm
After seeing du Sautoy's Algorithms show
July 15, 2018'''

import random
import time
import math

time1 = time.time()

POPN = 10000 #number of numbers to be sorted
comparisons = 0

nums = [random.randint(1,20000) for i in range(POPN)]
#print(nums)

def sort2(a,b):
    global comparisons
    newList = []
    while len(a)>0 or len(b)>0:
        if len(a)==0:
            min_b = b[0]
            newList.append(min_b)
            b.remove(min_b)
        elif len(b) == 0:
            min_a = a[0]
            newList.append(min_a)
            a.remove(min_a)
        else:
            min_a, min_b = min(a),min(b)
            comparisons += 1
            min_ab = min(min_a,min_b)
            if min_a < min_b:
                a.remove(min_ab)
            else:
                b.remove(min_ab)
            newList.append(min_ab)
        #newList.append(min(max_a,max_b))
        
        #b.remove(max_b)
        #print("sort2:",newList)
        #print("a:",a)
        #print("b:",b)

    return newList

def mergeSort(inputL):
    '''Sorts list inputL'''
    '''num = len(inputL)
    thelog = math.log(num,2)
    if thelog == int(thelog):
        levels = int(thelog)
    else:
        levels = int(thelog)# + 1
    print("thelog:",thelog,"levels:",levels)'''
    L = [[i] for i in inputL]
    
    while len(L)>1:
        #print(L)
        output = []
        #put items in 2-lists
        for i in range(0,len(L),2):
            if i == len(L)-1:
                output.append(L[i])
            else:
                output.append(sort2(L[i],L[i+1]))
        #print("Merge:",output)
        L = list(output)
    return L

M = mergeSort(nums)
#print(M)
print("comps:",comparisons)
print(time.time() - time1)

for i,m in enumerate(M[0]):
    if i < len(M) - 1:
        if m > M[i+1]:
            print(i,m)

with open("ten_thousand_list.txt","w") as f:
    for n in nums:
        f.write(str(nums)+',')

if sorted(nums) == M[0]:
    print("OK")
else:
    print("M:",M)
    print("sorted:",sorted(nums))
    print("not OK")
