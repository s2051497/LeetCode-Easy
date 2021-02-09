# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:28:08 2021

@author: Jeff
"""

# LeetCode #014 - Easy - Longest Common Prefix

        
        if len(strs) == 0:
            return ("")
        if len(strs) == 1:
            return(strs[0]) # strs -> ['flower']
                            # strs[0] -> 'flower'

        pref = strs[0]      #'flower'
        plen = len(pref)
        
        #如果 pref 不等於 i[從第二項的strs開始],我們縮減pref的長度(從最後面開始-1)
        for i in strs[1:]:
            while pref != i[0:plen]:
                pref = pref[0:plen-1]
                plen -= 1
                
                if plen == 0:
                    return("")
        return(pref)
    
    
    '''
        for i in strs[1:]:
            while pref != i[0:plen]:
                pref = pref[0:end-1]
                
                if pref == 0:
                    return("")
        return(pref)
    '''