#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/7/26 20:32
# @Author   :       YH
# @FILE     :       31_NextPermutation.py
# @Software :       PyCharm


# https://leetcode.cn/problems/next-permutation/solution/xiao-ying-wu-31-python-by-fvhk1d0cce-03lw/
'''
如何得到这样的排列顺序？这是本文的重点。我们可以这样来分析：
我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：在尽可能靠右的低位进行交换，需要从后向前查找
将一个 尽可能小的「大数」 与前面的「小数」交换。比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；然后需要将 5 之后的数重置为升序，得到 123546。显然 123546 比 123564 更小，123546 就是 123465 的下一个排列
'''

class Solution:
    def __init__(self):
        pass

    def nextPermutation(self, nums):
        # 0个、1个元素，直接返回
        N = len(nums)
        if N< 2:
            return nums
        
        # 找到从左到右最后一个升序的下标（即从右到左第一个升序的下标）
        for i in range(N-1, -1, -1):
            if i != N-1 and nums[i] < nums[i+1]:
                break
        print(i)

        # 说明nums一直降
        if i == 0 and nums[i] == max(nums):
            return nums.reverse()

        # 从后往前找nums[j]
        # 从后往前找第一个大于nums[i]的数nums[j]，如果没有大于nums[i]的数nums[j]，则j=i，交换个寂寞
        for j in range(N-1, i, -1):
            if nums[j] > nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]

        # 反转nums[i]后面的元素
        left, right = i+1, N-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 5]
    print(solution.nextPermutation(nums))