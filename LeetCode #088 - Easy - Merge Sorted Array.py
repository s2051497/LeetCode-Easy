# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:39:56 2021

@author: Adminstrator
"""

#%% LeetCode #088 - Easy - Merge Sorted Array
nums1.sorted()

#%%
nums1 = [1,2,3,4,0,0,0,0]
nums2 = [3,4,5,6]

nums3 = nums1 + nums2

while 0 in nums3:
    nums3.remove(0)

nums3.sort()
#%% Sol1
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1.sort()
        for i in range(n):
            nums1.remove(0)
        nums1 += nums2
        nums1.sort()
        
        '''
        nums1 += nums2
        while 0 in nums1:
            nums1.remove(0)
        nums1.sort()
        if nums1 == 0:
            nums1 = nums2
            return nums1
        elif nums2 == 0:
            return nums1
        '''
#%% Sol2.
def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
#%% Sol3.
https://www.youtube.com/watch?v=mwUYSherioU
設3個指針
A = num1的最後(非0)
B = num2的最後
L = num1的最後一位

#
if A > B:
    A放到L
else:
    B放到L
更新指針

#%%
def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
                

        
            
            
