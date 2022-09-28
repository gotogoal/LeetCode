class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0

		max_len = 0
		longest = ''  # 保存当前最长字符串
		for each_char in s:
			if each_char not in longest:
				longest += each_char
			else:
				# 开始存在重复字符，如果重复的正好是最后一个字符，那么我们就得从当前字符开始，重新创造longest
				if longest[-1] == each_char:
					longest = ''
				# 重复字符在前面，我们从重复字符下一个字符开始重新创建longest
				else:
					longest = longest[longest.index(each_char)+1:]
				longest += each_char

		if len(longest) > max_len:
			max_len = len(longest)

		return max_len


if __name__ == '__main__':
	solution = Solution()
	test = 'abcabcbb'
	print(solution.lengthOfLongestSubstring(test))
	test = 'bbbbb'
	print(solution.lengthOfLongestSubstring(test))
	test = 'pwwkew'
	print(solution.lengthOfLongestSubstring(test))
