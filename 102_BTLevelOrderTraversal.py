#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/9/6 11:23
# @Author   :       YH
# @FILE     :       102_BTLevelOrderTraversal.py
# @Software :       PyCharm


class TreeNode():
    # 节点类
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 建立二叉树是以层序遍历方式输入,节点不存在时以 'None' 表示
# nodeList 如 [1, 2, 3, 4, 5, None, 6, None, None, 7, 8]
def creatTree(nodeList):
    if nodeList[0] == None:
        return None
    head = TreeNode(nodeList[0])
    Nodes = [head]
    j = 1
    for node in Nodes:
        if node != None:
            node.leftChild = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
            Nodes.append(node.leftChild)
            j += 1
            if j == len(nodeList):
                return head
            node.rightChild = (TreeNode(nodeList[j])if nodeList[j] != None else None)
            j += 1
            Nodes.append(node.rightChild)
            if j == len(nodeList):
                return head


class Solution():
    # 树类
    def __init__(self):
        self.root = TreeNode()


    def add(self, val):
        # 为树加入节点
        node = TreeNode(val)
        # 如果树为空，就对根节点赋值
        if self.root.val == 0:
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            # 对已有的节点进行层次遍历
            while myQueue:
                treeNode = myQueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)

    # 层次遍历核心代码
    def levelOrder(self, root):
        if root == None:
            return
        queue = []
        queue.append(root)

        while queue:
            now_node = queue.pop(0)
            print(now_node.val)
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)


if __name__ == '__main__':
    # 主函数
    datas = [3, 9, 20, None, None, 15, 7]
    tree = Solution()
    for data in datas:
        # 逐个加入树的节点
        tree.add(data)

    print('递归实现前序遍历：')
    tree.levelOrder(tree.root)