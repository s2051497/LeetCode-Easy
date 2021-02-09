# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:44:11 2021

@author: Jeff
"""
# LeetCode #020 - Easy - Valid Parentheses
#%% Solution 1

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checklist = {"(":")","[":"]","{":"}"}
        stack = []

        for parenthese in s:
            if parenthese in checklist:
                stack.append(parenthese)               #將在checklist中的parenthese存入stack
            elif len(stack) == 0 or checklist[stack.pop()] != parenthese: 
                                                       #將stack的最後一個值 檢查是否在checklist裡面，並確認字典中對應的值是否正確
                return False                           # checklist[stack.pop()] => 字典右邊對應的值
                                                       #Ex: [{ ]}-> False

         # pop() 函式用於移除列表中的一個元素（預設最後一個元素），並且返回該元素的值。

            
         # 還有一種情況需考慮為只有括弧的右邊   Ex:"]" 
         # 因為不在checklist中 無法被append至stack中，因此也無法被pop
         # 因此需加入一判斷條件 len(stack) == 0 
        
        return len(stack) == 0
    


#%%
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #()最外層
        if "()" in s:
            if "[]" in s:
                if "{" in s and "}" not in s:
                    return False
                elif "}" in s and "{" not in s:
                    return False
                else:
                    return True
            elif "["  in s and "]" not in s:
                return False
            elif "]"  in s and "[" not in s:
                return False
            else:
                return True
        elif "("  in s and ")" not in s:
            return False
        elif ")"  in s and "(" not in s:
            return False
        else:
            return True
        
        
        #[] 最外層
        if "[]" in s:
            if "()" in s:
                if "{" in s and "}" not in s:
                    return False
                elif "}" in s and "{" not in s:
                    return False
                else:
                    return True
            elif "("  in s and ")" not in s:
                return False
            elif ")"  in s and "(" not in s:
                return False
            else:
                return True
        elif "["  in s and "]" not in s:
            return False
        elif "]"  in s and "[" not in s:
            return False
        else:
            return True
        
        #{} 最外層
        if "{}" in s:
            if "[]" in s:
                if "(" in s and ")" not in s:
                    return False
                elif ")" in s and "(" not in s:
                    return False
                else:
                    return True
            elif "["  in s and "]" not in s:
                return False
            elif "]"  in s and "[" not in s:
                return False
            else:
                return True
        elif "{"  in s and "}" not in s:
            return False
        elif "}"  in s and "{" not in s:
            return False
        else:
            return True
        
'''   
        if "[]" in s:
            if "()" in s:
                if "{" in s and "}" not in s:
                    return False
                else:
                    return True
            elif "(" in s and ")" not in s:
                return False
            else:
                return true
        elif "[" "]":
'''                
            
        
        
        
        
        '''
        for i in range(len(s)):
            
        
        currentInt = 
        nextInt = 
        
        if currentInt >= nextInt:
            total += currentInt
            else:
                total += total + (nextInt - currentInt)
        
        return total
    
            
        '''