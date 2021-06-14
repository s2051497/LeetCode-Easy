# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 22:22:05 2021

@author: Jeff
"""

# LeetCode #021 - Easy - Merge Two Sorted Lists
#%% References
https://desolve.medium.com/%E5%BE%9Eleetcode%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-4-6a631eb50da3
http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html
http://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html
https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d

#%%
#Q:
l1 = [1,2,4]
l2 = [1,3,4]


# Def of ListNode
class ListNode():
    def __init__(self,data):
        # store data
        self.val = data
        # store the next item
        self.next = None

# 初始化一個Node, dummy&prev都指向該節點，但是dummy需要不斷擴充套件，因為結果不是一個節點能完成的。
        dummy = ListNode(0)
        prev = dummy
        
        while l1 and l2: # <=======> if not (l1 and l2)
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
            
        if l1 == None:
            prev.next = l2
        elif l2 == None:
            prev.next = l1
        
        return dummy.next
    '''
    dummy = [0,1,1,2,3,4,4]
    dummy.next = [1,1,2,3,4,4]
    prev = [4,4]
    prev.next = [4]
    '''
    