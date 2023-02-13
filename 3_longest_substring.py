class Solution(object):
	def __init__(self):
		pass
	
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0

		max_len = 0
		# 保存当前最长字符串
		longest = ''
		for each_char in s:
			if each_char not in longest:
				longest += each_char
			else:
				# 重复字符在前面, 我们从重复字符下一个字符开始重新创建longest
				longest = longest[longest.index(each_char)+1:]
				# 把当前字符添加到最长字符串里
				longest += each_char

			# 判断最长
			if len(longest) > max_len:
				max_len = len(longest)

		return max_len
	
	# 暴力法:两个循环
	def lengthOfLongestSubstring_stupid(self, s):
		max_len = 0
		n = len(s)
		# 遍历
		for i in range(n):
			tmp = []
			# 从当前字符到最后
			for j in range(i, n):
				if s[j] not in tmp:
					tmp.append(s[j])
				else:
					if len(tmp) > max_len:
						max_len = len(tmp)
					break
		return max_len


if __name__ == '__main__':
	solution = Solution()
	test = 'abcabcbb'
	print(solution.lengthOfLongestSubstring_stupid(test))
	print(solution.lengthOfLongestSubstring(test))
	test = 'bbbbb'
	print(solution.lengthOfLongestSubstring_stupid(test))
	print(solution.lengthOfLongestSubstring(test))
	test = 'pwwkew'
	print(solution.lengthOfLongestSubstring_stupid(test))
	print(solution.lengthOfLongestSubstring(test))
