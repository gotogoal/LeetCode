class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __index__(self):
        pass

    def detectCycle(self, head):
        fast, slow = head, head
        # 第一次相遇
        while True:
            if not (fast and fast.next):
                return
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        # 从头开始每次一步和从相遇结点开始每次一步到相遇, 正好就是入口结点, 具体参考下面连接进行推理
        # https://zhuanlan.zhihu.com/p/410356891
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast


if __name__ == '__main__':
    pass

