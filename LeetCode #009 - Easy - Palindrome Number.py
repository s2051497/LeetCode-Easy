# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:20:16 2021

@author: Jeff
"""
# LeetCode #009 - Easy - Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
#%% Solution 1 - Reverse the number as string

        return(str(x) == str(x)[::-1])
  
#%% Solution 2 - Reverse the number fully

'''
1. create a backwards copy of the number
2. if backwards copy is the same, return true
----------------
121
121 -> True

10
01 -> False

-121
121- -> False
-----------------
Explanation:
    c = 1234 # Copy number
    b = 0    # Backwards number
    
    1234 % 10 -> 4
    1234 / 10 -> 123 #(not 123.4 due to python version)
    c -> 123
    b -> 0 *10 +4 
      -> 4
    
    123 % 10 -> 3
    123 / 10 -> 12
    c -> 12
    b -> 4 * 10 + 3
      -> 43
    
    ....
    ....
    
    b -> 4321
    
# Test Cases:
  negative numbers -> False
  0 -> true
  
  1210 -> False
  b = 121 
  
# Time Complexity
Time O(n), O(log(k)) # The Same

n is the number of digits in x
k is the size of the number     log 1000 -> 3, log 100 -> 2

# Space Complexity
O(1)

b&c are intergers 
-------------------
'''

#Code
        if x < 0:
            return False
        
        c = x
        b = 0

        while c:
            b = b * 10 + c % 10
            c /= 10                #c = c / 10
        return b == x
    

#%% Solution 3 - Reverse half of the number 

'''
1234
12
43

1221
12
12

12321
123
123

1. reverse half of the number, compare it with our original number

# Test Cases

Even    x  b
1221 -> 12 12 -> true
1231    12 13    false
1321    1  123   false

End of zero

1230    1  32   False
1210    1  12
0121    1  12


Odd     x  b    b/10
12321   12 123  12      > true
12322   12 223  22      > fa;se

# Time Complexity
O(n)
n is the number of digits

# Space Complexity
O(1)

we only store 1 extra ineger so we're not haveing any other data structures.

This soultion is more slittly efficient than the other one in terms of time complexity 
it's still O(n) but you only have to do it iteration for half of the number of digits 

'''
# Code
        if x < 0 or (x % 10 == 0 and x != 0): #the number ends of 0, and not 0
            return False

        b = 0

        while x > b: # the loop stops when b become equal to x or bigger than x
            b = b * 10 + x % 10
            x /= 10
        return x == b or x == b /10