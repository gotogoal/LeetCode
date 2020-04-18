import sys


class Solution:
    def __init__(self):
        pass

    def coinChange(self, coins, amount):
        """
        :param coins: 硬币的种类列表，如[2, 5, 7]
        :param amount: 总金额
        :return:用最少的硬币数组成总金额
        """
        max_size = sys.maxsize
        result = [max_size for _ in range(amount+1)]
        result[0] = 0
        for num in range(1, amount + 1):
            temp = []
            for each_coin in coins:
                if num - each_coin < 0:
                    temp.append(max_size)
                else:
                    temp.append(result[num - each_coin] + 1)

            result[num] = min(temp)

        if result[-1] >= max_size:
            return -1
        else:
            return result[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([2, 5, 7], 27))
    print(solution.coinChange([2], 3))
    print(solution.coinChange([2, 5, 7], 27))
