class Solution:
    def __init__(self):
        pass

    # 写螺旋数组问题，也是要保证始终按照一个区间去写，就是，不管是从左到右，还是从上到下，都要保证区间一直（左闭右开）
    # 填充上行从左到右
    # 填充右列从上到下
    # 填充下行从右到左
    # 填充左列从下到上
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        
        # 初始数字 
        number = 1
        
        left, right, up, down = 0, n-1, 0, n-1
        while left < right and up < down:
            # 从左向右:行不变-up, 列自增
            for i in range(left, right):
                matrix[up][i] = number
                number += 1
            
            # 从上到下:行自增,列不变-right
            for i in range(up, down):
                matrix[i][right] = number
                number += 1
            
            # 从右向左:行不变-down, 列递减
            for i in range(right, left, -1):
                matrix[down][i] = number
                number += 1
            
            # 从下向上:列不变-left, 行递减
            for i in range(down, up, -1):
                matrix[i][left] = number
                number += 1
            
            left += 1
            right -= 1
            up += 1
            down -= 1

        if n % 2 != 0:
            matrix[ n//2 ][ n//2 ] = number
        
        return matrix


if __name__ == '__main__':
    solution = Solution()
    n = 3
    print(solution.generateMatrix(n))
