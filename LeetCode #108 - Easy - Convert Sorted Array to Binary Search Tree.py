# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:37:55 2021

@author: Jeff
"""

#%% LeetCode #108 - Easy - Convert Sorted Array to Binary Search Tree
https://www.youtube.com/watch?v=0K0uCMYq5ng

#%% Sol1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left,right):
            middle = (left+right) // 2

            if left > right:
                return None
            
            root = TreeNode(nums[middle])
            root.left = helper(left, middle - 1)
            root.right = helper(middle + 1, right)
            return root
        return helper(0,len(nums) - 1)#-1 is because the 0 which is not included.
