import math
import sys


class Solution:
    def __init__(self):
        pass

    def numSquares(self, n):
        max_square = int(math.sqrt(n))
        nums = [_ ** 2 for _ in range(1, max_square+1)]

        maxsize = sys.maxsize

        dp = [maxsize] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in nums:
                if i - j >= 0:
                    dp[i] = min(dp[i-j] + 1, dp[i])
                else:
                    dp[i] = min(dp[i], maxsize)
        # print(dp)
        if dp[-1] >= maxsize:
            return -1
        else:
            return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(12))
    print(solution.numSquares(13))
