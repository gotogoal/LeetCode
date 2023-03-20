# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head:
            return head
        
        # 临时节点
        Lhead = ListNode(0)
        Lhead.next = head

        # 用于寻找m处的节点以及m的前驱节点
        pre = Lhead
        cur = head

        # 当 m=1 时, 已经找到了 m 节点与 m 的前驱
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        # 将找到的 m 节点与 m 的前驱先保存起来
        m_pre, m_cur = pre, cur

        # 开始对 n 段长的节点进行反转:即对 cur 后的n(已经发生变化了的n)个节点反转
        # 反转后的头结点是 pre, 而 cur 指向最后那短剑结点
        while n:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            n -= 1

        # 反转完成后, 将链表连接起来，链表题建议画图理解
        m_pre.next = pre
        m_cur.next = cur
    
        return Lhead.next


if __name__ == '__main__':
    solution = Solution()
    n1 = ListNode(val=1)
    n2 = ListNode(val=2)
    n3 = ListNode(val=3)
    n4 = ListNode(val=4)
    n5 = ListNode(val=5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    head = n1
    # 开始反转
    head_new = solution.reverseList(head, n2, n3)
    cur = head_new
    while cur:
        print(cur.val)
        cur = cur.next