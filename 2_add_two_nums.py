# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def add_two_numbers(self, l1, l2):
		current = head = ListNode(0)
		flag = 0

		while l1 or l2:
			x = l1.val if l1 else 0
			y = l2.val if l2 else 0
			sum_temp = x + y + flag
			flag = sum_temp // 10

			current.next = ListNode(sum_temp % 10)
			current = current.next
			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next

		if flag == 1:
			current.next = ListNode(1)

		return head.next


if __name__ == '__main__':
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)
	print(l1.val, l1.next.val, l1.next.next.val)

	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)
	print(l2.val, l2.next.val, l2.next.next.val)

	solution = Solution()
	head = solution.add_two_numbers(l1, l2)
	current = head
	while current:
		print(current.val)
		current = current.next

