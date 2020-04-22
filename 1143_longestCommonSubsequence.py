# https://blog.csdn.net/ggdhs/article/details/90713154
class Solution:
    def __init__(self):
        pass

    # 并不要求连续
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

    # 求最长公共子串长度，这就要求连续了
    def longestCommonSubstring(self, text1, text2):
        m = len(text1)
        n = len(text2)

        result = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
                else:
                    # 不相等的话就直接赋值为0了，重新开始求最长公共子串
                    pass

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence('helloworld', 'loop'))
    print(solution.longestCommonSubstring('helloworld', 'loop'))
