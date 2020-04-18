class Solution:
    def __init__(self):
        pass

    # DP
    def canJump(self, nums):
        result = [False] * len(nums)
        result[0] = True
        for i in range(1, len(nums)):
            for j in range(i):
                if result[j] and nums[j] >= (i - j):
                    result[i] = True
                    break  # 很重要，容易遗忘

        return result[-1]

    # 贪心
    def canJump_2(self, nums):
        # max_idx记录每次能达到的最大位置
        max_idx = 0
        n = len(nums)
        for i in range(n):
            # 如果能达到就return True
            if max_idx >= n - 1:
                return True
            if i > max_idx:
                return False
            # 每次更新最大可达位置
            max_idx = max(max_idx, i + nums[i])
        return False



if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump([2, 3, 1, 1, 4]))
    print(solution.canJump([3, 2, 1, 0, 4]))
