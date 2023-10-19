#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2023/5/5 18:07
# @Author   :       YH
# @FILE     :       143_ReorderList.py
# @Software :       PyCharm


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self):
        pass

    # 方法一：将链表节点用数组保存下来，然后按照题目顺序重新连接起来。注意存的是节点，而不是链表的值
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i == j:
                break
            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None

    # 方法二：先寻找链表中点，再对链表后半部进行翻转，然后合并链表。好家伙！一道顶三道，寻找链表中点，翻转链表，合并链表
    def reorderList2(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def mergeList(self, l1, l2):
        while l1 and l2:
            l1_temp = l1.next
            l2_temp = l2.next

            l1.next = l2
            l1 = l1_temp

            l2.next = l1
            l2 = l2_temp