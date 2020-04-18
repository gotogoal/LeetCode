# https://blog.csdn.net/qq_41359051/article/details/86623571
class Solution:
    def __index__(self):
        pass

    # 递归实现：从字符串的尾部开始
    def get_edit_distance(self, strA, strB):
        if len(strB) == 0:  # 考虑字符串B为空字符串时
            return len(strA)
        elif len(strA) == 0:  # 考虑字符串A为空字符串时
            return len(strB)
        else:
            if strA[-1] == strB[-1]:  # 当最后一个字母相同时
                distance = self.get_edit_distance(strA[:-1], strB[:-1])

            else:  # 当最后一个字母不同时
                distance = min(  # 只保留最优解的结果
                    self.get_edit_distance(strA, strB[:-1]) + 1,  # 插入操作
                    self.get_edit_distance(strA[:-1], strB) + 1,  # 删除操作
                    self.get_edit_distance(strA[:-1], strB[:-1]) + 1,  # 替换操作
                )

            return distance

    # 迭代实现
    # 迭代其实是递归的反向实现。使用递归时，我们要从字符串的最后一个字母入手，迭代则需要从第一个字母入手
    def get_edit_distance_2(self, strA, strB):
        d = [[0] * (len(strB) + 1) for __ in range(len(strA) + 1)]

        # 当 strB 为空字符串时
        for i in range(len(strA) + 1):  # 'a' 为填充物，表示从 strA 为空字符串的时候开始
            d[i][0] = i

        # 当 strA 为空字符串时
        for j in range(len(strB) + 1):  # 'a' 为填充物，表示从 strB 为空字符串的时候开始
            d[0][j] = j

        # 注意range的第一个参数是1，因为我们得从第二行第二列的位置开始填表
        # 第一行与第一列已经在前面初始化了
        for i in range(1, len(strA) + 1):
            for j in range(1, len(strB) + 1):
                if strA[i - 1] == strB[j - 1]:  # 与递归不同，不是从最后一个字母开始比较
                    d[i][j] = d[i - 1][j - 1]
                else:
                    # 在插入、删除、替换操作中保留最优解
                    d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + 1)

        return d[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"

    solution = Solution()
    print(solution.get_edit_distance(word1, word2))
