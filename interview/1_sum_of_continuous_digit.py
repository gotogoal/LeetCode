class Solution(object):
    def sum_of_continuous_digit(self, num):
        """
        :param num:输入一个正整数(num)，若该数能用几个连续正整数之和表示，则输出所有可能的正整数序列（高德）
        :return:所有可能的连续数字之和
        """

        '''
        思路：
            首先这个num的连续数字之和的start数字肯定不会从median开始，如果从median开始的话，连续数字之和必定超过num
            也就是下面的第一个循环，确定了start
            end也好确定，也就是我们的end = median，最后利用求和公式进行判断

        '''
        result = []
        median = (num + 1) // 2
        for start in range(1, median):
            for end in range(start, median+1):
                if (start + end) * (end - start + 1) // 2 == num:
                    result.append(tuple(range(start, end+1)))

        return result


if __name__ == '__main__':
    solution = Solution()
    while True:
        N = int(input('Please input a num:'))
        print(solution.sum_of_continuous_digit(N))

