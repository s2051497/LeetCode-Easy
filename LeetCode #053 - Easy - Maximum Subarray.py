# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:07:25 2021

@author: Jeff
"""
# LeetCode #053 - Easy - Maximum Subarray

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
https://www.youtube.com/watch?v=5WZl3MMT0Eg&t=1s
#%% 
nums = [-2,1,-3,4,-1,2,1,-5,4]
#%%
a = 10
b = 20
print(max(a,b))
#%% Sol1.

curMax = 0
Maxmax = nums[0]
for i in nums:
    print('curMax',curMax)            
    if curMax < 0:
        curMax = 0
    curMax += i
    
    Maxmax = max(curMax,Maxmax) 
    print('Maxmax',Maxmax)
#return Maxmax
