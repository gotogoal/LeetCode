class Solution:
    def __init__(self):
        pass

    def countBits(self, num):
        if num == 0:
            return [0]

        elif num == 1:
            return [0, 1]

        result = [0, 1]
        for i in range(2, num + 1):
            if i % 2 == 0:
                # 当前数是偶数的话，与i / 2的二进制表示中1的个数一致
                result.append(result[i//2])
            else:
                # 当前数是奇数的话，比i / 2的二进制表示中1的个数多1
                result.append(result[i//2]+1)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(11))
