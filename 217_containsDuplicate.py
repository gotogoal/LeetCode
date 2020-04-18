class Solution:
	def containsDuplicate(self, nums):
		if len(set(nums)) == len(nums):
			return False
		else:
			return True


if __name__ == '__main__':
	solution = Solution()
	print(solution.containsDuplicate([1, 2, 3, 1]))
	print(solution.containsDuplicate([1, 2, 3, 4]))
	print(solution.containsDuplicate([1, 1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
