#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/11/16 14:01
# @Author   :       YH
# @FILE     :       160_IntersectionOfTwoLinkedLists.py
# @Software :       PyCharm


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def __init__(self):
        pass
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = headA
        B = headB
        while A!=B:
            if A:
                A = A.next
            else:
                A = headB
            
            if B:
                B = B.next
            else:
                B = headA
        return A