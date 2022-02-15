class Solution:

	def __init__(self):
		pass

	def longestPalindrome(self, s):
		"""
        :type s: str
        :rtype: str
        """
		n = len(s)
		if n == 1:
			return s
		# 长度大于1，则至少一个字符是回文的
		begin = 0
		max_len = 1
		# dp[i][j] 表示 s[i..j] 是否是回文串
		dp = [[False] * n for _ in range(n)]
		# 自己到自己肯定是回文
		for i in range(n):
			dp[i][i] = True
			
		# 枚举回文子串的长度 2->n
		for L in range(2, n+1):
			# 枚举左边界，左边界的上限设置可以宽松一些
			for i in range(n):
				j = L + i - 1
				# 右边界最大值为:j=n-1
				if j > n-1:
					break

				if s[i] != s[j]:
					dp[i][j] = False
				else:
					# j - i 最大为2, L最大为3时
					if j - i < 3:
						dp[i][j] = True
					else:
						dp[i][j] = dp[i + 1][j - 1]

				# 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
				if dp[i][j] and j - i + 1 > max_len:
					max_len = j - i + 1
					begin = i

		return s[begin:begin + max_len]

					
if __name__ == '__main__':
	solution = Solution()
	s = "cstgvkbrxacmpxdxxktktvpdzcuxmnhvuxdgsmskgeeawzeikhtmhdvnccbrgifpzmiuytfmeyfoxsntrdtxeuxcqsndexbgfxnthqwveujqzemloooyddparbjcuiwpopjwvvmwblsamkhjhlnoxinkpsempexmipifsfwzxbetgvfnkngzxcpizwctpdlpngjpyovmjllxfiwktghkxvyelwjwdztujmunijfsfdvmhgqhlpouewgyznphlmccjmqaqncwbeqheohibafqfunfywmrvqvjygjwqoclijwkcfiuaiymeagdbwyejnvtosxylptbtyoahfzfmwzrkhzdamknleroffmsqcaryibamgdpcumlhrblypddzhaxfeztokgogzgvpfvlmetiwsamhdidmvxavleryfyakendwrbslcavlqkerrnvpuzhdgwzuyorxzbkzhxhpbvkflgxouvaavxrdzsjlgrmogzvlhhdidldsxqhrqlryaanffhxnutcycnczuedtrwcnfiqrtoafvdfnfhxhyjivzalozrbrajboecfyalisxxanduzraqdrbzsbkobaieqpzcawrunxucypqyjnmrlrlivrrwwhdpekeelsphhunzbhkkejvqfopjsuholutgmtnleqdrntbqgrobnuhqpdkbjtikijkdiwqvnxgajaaqgswrdamzv"
	print(solution.longestPalindrome(s))
			