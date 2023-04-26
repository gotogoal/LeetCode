class Solution:
    def __init__(self):
        pass

    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)                


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
