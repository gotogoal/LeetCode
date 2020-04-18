class Solution:
	def tribonacci(self, n: int) -> int:
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
				a = b
				b = c
				c = T_n
		return T_n


if __name__ == '__main__':
	solution = Solution()
	n = 25
	print(solution.tribonacci(n))
