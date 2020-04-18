class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __index__(self):
        pass

    def hasCycle(self, head):
        set = []
        cur = head
        while cur:
            if cur in set:
                return True

            set.append(cur)
            cur = cur.next

        return False

    # 方法二：快慢指针，如果存在环，两者必偶遇
    # 因为快指针每次走两步，慢指针每次一步，快指针每次都可以追赶一步
    def hasCycle_2(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False


if __name__ == '__main__':
    list_ = [2, 0, 4]
    head = ListNode(3)
    cur = head
    for x in list_:
        new_node = ListNode(x)
        cur.next = new_node
        cur = new_node

    # 加上环，指向第二个节点
    cur.next = head.next

    solution = Solution()
    print(solution.hasCycle(head))
    print(solution.hasCycle_2(head))

