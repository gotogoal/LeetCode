class Solution:
    def __init__(self):
        pass

    def countBits(self, num):
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1
                    ]
        result = [0, 1]
        for i in range(2, num + 1):
            if i % 2 == 0:
                result.append(result[i//2])
            else:
                result.append(result[i//2]+1)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(11))
