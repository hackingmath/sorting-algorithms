'''Bubble Sort'''

import random
import time

time1 = time.time()

comparisons = 0
POPN = 10000
nums = [random.randint(1,20000) for i in range(POPN)]

for j in range(POPN-2):
    for i in range(j,POPN-2):
        comparisons += 1
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]

print("comps:",comparisons)
print(time.time() - time1)
