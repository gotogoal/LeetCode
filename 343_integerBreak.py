class Solution:
    def __init__(self):
        pass

    def integerBreak(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            dp = [0] * (n + 1)
            dp[1] = 1
            # 如计算dp[4]，则i = 4，j = 1.2.3
            # j = 1，即1 + 3：j * dp[4 - 1]
            # j = 2，即2 + 2：j * dp[4 - 2]
            # j = 3, 即3 + 1：j * dp[4 - 3]
            # j * (i - j)表示只拆成2个整数
            for i in range(2, n+1):
                for j in range(1, i // 2 + 1):
                    dp[i] = max(dp[i], j * (i-j), j * dp[i-j])

            return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.integerBreak(10))
    for i in range(2, 20):
        print('i = {}:{}'.format(i, solution.integerBreak(i)))
