#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/9/28 9:46
# @Author   :       YH
# @FILE     :       25_ReverseNodesInkGroup.py
# @Software :       PyCharm


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://blog.csdn.net/qq_45905045/article/details/124331587
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        a = head
        b = head
        # 区间 [a, b) 包含 k 个待反转元素：k次循环
        for i in range(k):
            # 不足 k 个, 不需要反转: base case
            if not b:
                return head
            b = b.next
        # 反转前 k 个元素
        newHead = self.reverse(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return newHead

    # 反转 a 和 b 之间的节点
    def reverse(self, a, b):
        pre = None
        cur = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre