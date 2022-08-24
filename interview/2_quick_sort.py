class Solution(object):
    def __init__(self):
        pass

    def quick_sort(self, lists, low, high):
        if low < high:
            pi = self.partition(lists, low, high)
            self.quick_sort(lists, low, pi-1)
            self.quick_sort(lists, pi+1, high)
        return lists

    def partition(self, lists, i, j):
        pivot = lists[i]
        while i < j:
            while i < j and lists[j] >= pivot:
                j -= 1
            lists[i] = lists[j]
            while i < j and lists[i] <= pivot:
                i += 1
            lists[j] = lists[i]
        lists[j] = pivot
        return j


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 9, 1, 2, 3, 9, 4]
    print(solution.quick_sort(nums, 0, len(nums)-1))
