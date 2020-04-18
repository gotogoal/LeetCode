class Solution:
    def __init__(self):
        pass

    def uniquePaths(self, m, n):
        matric = [[1] * n for _ in range(m)]

        # for i in range(m):
        #     matric[i][0] = 1
        # for j in range(n):
        #     matric[0][j] = 1
        # print(matric)

        for i in range(1, m):
            for j in range(1, n):
                matric[i][j] = matric[i-1][j] + matric[i][j-1]

        return matric[m-1][n-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 2))
    print(solution.uniquePaths(7, 3))
