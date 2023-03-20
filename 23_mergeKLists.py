#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2023/3/10 19:49
# @Author   :       YH
# @FILE     :       23_mergeKLists.py
# @Software :       PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def __init__(self):
        pass

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodeList = []
        # 我们先遍历一次所有的链表中的元素。然后将元素全部放在一个数组里面
        for i in range(len(lists)):
            currentNode = lists[i]
            while currentNode:
                nodeList.append(currentNode)
                currentNode = currentNode.next

        # 接着对这个数组进行排序
        nodeList = sorted(nodeList, key=lambda x: x.val)

        # 最终将排序后的数组里面的所有元素链接起来
        pHead = ListNode(0)
        currentNode = pHead
        for i in range(len(nodeList)):
            currentNode.next = nodeList[i]
            currentNode = currentNode.next

        return pHead.next