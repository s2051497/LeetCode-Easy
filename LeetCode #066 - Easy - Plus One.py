# -*- coding: utf-8 -*-
"""
Created on Mon May 31 12:16:26 2021

@author: Jeff
"""
# LeetCode #066 - Easy - Plus One

#%% Sol1.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        '''
        Step1.將list轉為整數
        Step2.將整數+1
        Step3.將整數轉為list
        '''
        #Step1. 
        s = [str(x) for x in digits]
        final_int = int("".join(s))

        #Step2. 
        final_int += 1

        #Step3.
        final_list = [int(x) for x in str(final_int)]
        return final_list


#%%
final = ans + 1    
return final

#%% Convert int into list
n = 43365644 
digits = [int(x) for x in str(n)]
#%% Convert list into int
integers = [1, 2, 3]

strings = [str(integer) for integer in integers]
a_string = "".join(strings)
an_integer = int(a_string)

print(an_integer)
#%%
a = [12,15,17]
for i in a:
    print(i,end="")
    
#%%

1.將list轉為整數
2.將整數+1
3.將整數轉為list

#Step1. 
s = [str(x) for x in digits]
final_int = int("".join(s))
return final_int

#Step2. 
final_int += 1

#Step3.
final_list = [int(x) for x in str(final_int)]
