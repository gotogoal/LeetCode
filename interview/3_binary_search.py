class Solution(object):
    def __init__(self):
        pass

    def bi_search(self, list_nums, num):
        if len(list_nums) == 0:
            return False

        mid_index = (len(list_nums) + 1) // 2

        mid_num = list_nums[mid_index]
        if num == mid_num:
            return True
        else:
            if mid_num > num:
                return self.bi_search(list_nums[0: mid_index], num)
            else:
                return self.bi_search(list_nums[mid_index + 1:], num)


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 7, 7, 9]
    num = 5
    num = 10
    print(solution.bi_search(nums, num))
