class Solution:
	def longestPalindrome(self, s: str) -> str:
		"""马拉车算法 --- 时间复杂度降低到线性"""
		S = "^#"
		for i in range(0, len(s)):
			S = S + s[i] + "#"
		S = S + "$"
		print(S)
		P = [0 for i in range(0, len(S))]
		print(P)
		M = 0
		R = 0
		for i in range(1, len(S) - 1):
			j = M * 2 - i
			if R > i:
				if R - i > P[j]:
					P[i] = P[j]
				else:
					P[i] = R - i
			else:
				P[i] = 0
			# print("P[i]:" + str(P[i]))
			# print("i:" + str(i))
			# print("S[i]" + str(S[i]))
			while S[i + P[i] + 1] == S[i - P[i] - 1]:
				P[i] = P[i] + 1
			# print(P[i])

			if i + P[i] > R:
				R = i + P[i]
				M = i
		# print(P)
		Center = 0
		maxl = 0
		for i in range(1, len(S) - 1):
			if P[i] >= maxl:
				maxl = P[i]
				Center = i

		start = int((Center - maxl) / 2)
		end = start + maxl
		# print(start)
		# print(end)
		return s[start:end]


if __name__ == '__main__':
	solution = Solution()
	print(solution.longestPalindrome('babad'))
	print(solution.longestPalindrome('cbbd'))
	print(solution.longestPalindrome('ac'))
