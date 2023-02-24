# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head, left, right):
        if not head:
            return head
        pre = None
        cur = head
        while cur != left:
            pre = cur
            cur = cur.next
        # [left,right) 之间的反转
        new = self.reverse(left, right)
        
        # right 由于没被反转,直接追加到cur节点后
        if pre:
            pre.next = right
        else:
            head = right
        
        # right 后的节点保持不变
        tmp = right.next
        
        # 反转后的头结点至于 right 后
        right.next = new
        
        # right 后的节点置给反转后的链表尾部-即 left 后 
        left.next = tmp
        return head
    
    def reverse(self, left, right):
        pre = None
        cur = left
        while cur!=right:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


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