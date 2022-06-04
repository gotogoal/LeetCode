#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/4/18 7:55
# @Author   :       YH
# @FILE     :       206_reverse_linked_list.py.py
# @Software :       PyCharm


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':
    solution = Solution()
    n1 = ListNode(val=1)
    n2 = ListNode(val=2)
    n3 = ListNode(val=3)
    n1.next = n2
    n2.next = n3
    n3.next = None
    head = n1
    # 开始反转
    head_new = solution.reverseList(head)
    print(head_new.val, head_new.next.val, head_new.next.next.val)