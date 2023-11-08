# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		temp = dict()
		for index, value in enumerate(nums):
			if value in temp:
				return [temp[value], index]
			else:
				temp[target - value] = index

		return None


if __name__ == '__main__':
	solution = Solution()
	nums = [2, 7, 11, 15]
	target = 18
	print(solution.twoSum(nums, target))
