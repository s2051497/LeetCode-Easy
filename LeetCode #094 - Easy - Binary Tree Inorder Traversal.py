# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:55:07 2021

@author: Adminstrator
"""

#%% LeetCode #094 - Easy - Binary Tree Inorder Traversal
#  3 Types of Depth-first orders (Binary Tree Traversal)
1. Pre-order (N-L-R)
2. In-order (L-N-R)
3. Post-order (L-R-N)

# In order (LNR)
Step1. 若Node的左端點有值，持續下去
       若Node左端點沒有值，將此數值紀錄下來，繼續檢查右端點是否有值
       若右端點有數值

