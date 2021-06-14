# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:21:54 2021

@author: Jeff
"""

# LeetCode #101 - Easy - Symmetric Tree
#%% Sol1.
https://www.youtube.com/watch?v=ZXi6HLVe4uk

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is  None:
            return True
        
        return self.isSym(root.left,root.right)
    
    def isSym(self,left,right):
        if left is None and right is None:

            return True

        if left is None or right is None or left.val != right.val:

            return False

        return self.isSym(left.left,right.right) and self.isSym(left.right,right.left) 
#%% Sol2.
https://www.youtube.com/watch?v=qNH6fFdb6Hs
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True
        
        return self.isMirror(root.left,root.right)
    
    def isMirror(self,leftroot,rightroot):
        if leftroot and rightroot: # not None
            return leftroot.val == rightroot.val and self.isMirror(leftroot.left,rightroot.right) and self.isMirror(leftroot.right,rightroot.left)
        return leftroot == rightroot

    
#%%
檢查左節點的左child是否與右節點的右child一致
檢查左節點的右child是否與右節點的左child一致

