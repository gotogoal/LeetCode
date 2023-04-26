'''
给你一个 m 行 n 列的矩阵 matrix, 请按照 顺时针螺旋顺序, 返回矩阵中的所有元素
'''
class Solution:
    def __init__(self):
        pass

    # 核心是每次遇到新的边界时，顺时针修改移动方向，并且将老边界内移
    def spiralOrder(self, matrix):
        # 空
        if not matrix or not matrix[0]:
            return []
        # 行
        m = len(matrix)
        # 列
        n = len(matrix[0])
        res = []
        
        left, right, up, down = 0, n-1, 0, m-1
        x, y = 0, 0
        cur_d = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len(res) != m * n:
            res.append(matrix[x][y])

            # 从左向右到达右边界
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1

            # 从上到下到达底
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1

            # 从右到左边界
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1

            # 从下到上到达上边界
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1

            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]

        return res


    # 思路: 对于这个列表矩阵, 先输出第一行并将其pop除去, 然后将矩阵逆时针旋转90度，继续输出第一行并将其pop出去，递归的执行上述操作直至矩阵为空
    def spiralOrder2(self, matrix):
        ret = []
        while matrix:
            ret.extend(matrix.pop(0))
            # 逆时针旋转
            matrix = [list(x) for x in zip(*matrix)][::-1]
        return ret
            

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3],[5,6,7],[9,10,11]]
    print(solution.spiralOrder(matrix))
    print(solution.spiralOrder2(matrix))
