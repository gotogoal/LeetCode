class Solution(object):
    def __init__(self):
        pass

    def quick_sort(self, nums):
        # 终止条件
        if len(nums) < 2:
            return nums
        mid = nums[len(nums) // 2]
        left, right = [], []
        nums.remove(mid)
        for i in nums:
            if i >= mid:
                right.append(i)
            else:
                left.append(i)

        return self.quick_sort(left) + [mid] + self.quick_sort(right)


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 9, 1, 2, 3, 9, 4]
    print(solution.quick_sort(nums))
