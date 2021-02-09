# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:48:44 2021

@author: Jeff
"""

# LeetCode #013 - Easy - Roman to Integer

#%% solution 1
# https://www.youtube.com/watch?v=nCDoMK-E7mc

s = input()        
def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    romantoint = {'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
    total = 0
    
    for i in range(len(s)):
        if i+1 != len(s) and romantoint[s[i]] < romantoint[s[i+1]]:
            total = total - romantoint[s[i]]
        else:
            total = total + romantoint[s[i]]
    return total
 
print(romanToInt(s))

#%% Solution 2
        romanToInt = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        
        for i in range(len(s)):
            if i > 0 and romanToInt[s[i]] > romanToInt[s[i-1]]:
                total += romanToInt[s[i]] - 2 * romanToInt[s[i-1]]
            else:
                total += romanToInt[s[i]]
        return total
    
        
