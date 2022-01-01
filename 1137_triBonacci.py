# 第 N 个泰波那契数
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

class Solution:
	def __init__(self):
		pass

	def tribonacci(self, n):
		if n == 0:
			return 0
		elif n == 1 or n == 2:
			return 1
		else:
			a = 0
			b = 1
			c = 1
			for i in range(3, n+1):
				T_n = a + b + c
				a, b, c = b, c, T_n
				c = T_n
		return T_n


if __name__ == '__main__':
	solution = Solution()
	n = 25
	print(solution.tribonacci(n))
