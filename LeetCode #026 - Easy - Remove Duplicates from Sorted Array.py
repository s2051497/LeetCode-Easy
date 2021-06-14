# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:32:11 2021

@author: Jeff
"""

# LeetCode #026 - Easy - Remove Duplicates from Sorted Array
#%% References
https://blog.csdn.net/coder_orz/article/details/51589013
https://ithelp.ithome.com.tw/articles/10213266
https://medium.com/@urdreamliu/26-%E5%9C%96%E8%A7%A3-remove-duplicates-from-sorted-array-cbee5b2d4df8
#%%
# Question 
# Input
nums = [1,1,2,3]

# Output
# 2, nums = [1,2]

#%% Sol.1
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer = 0
        if not nums:
            return 0
        
        for i in range(1,len(nums)):
            if nums[i] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[i]
        return pointer + 1
#%% Sol.2     
        if not nums:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
                
