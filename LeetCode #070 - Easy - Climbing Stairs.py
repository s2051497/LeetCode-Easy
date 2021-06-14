# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:06:17 2021

@author: Jeff
"""

# LeetCode #070 - Easy - Climbing Stairs
https://www.youtube.com/watch?v=IRfKXVN2f2g
https://www.youtube.com/watch?v=5o-kdjv7FD0
#%% Sol1.
# 第n階的機率 = n-1階的機率 + n-2階的機率
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        path = {1:1,2:2}
        for i in range(3,n+1):
            path[i] = path[i-1] + path[i-2]
        return (path[n])