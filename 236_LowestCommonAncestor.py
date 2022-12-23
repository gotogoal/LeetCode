#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/10/31 20:29
# @Author   :       YH
# @FILE     :       236_LowestCommonAncestor.py
# @Software :       PyCharm


'''
二叉树的查找问题一般都是从左右子树递归去解决,也往往都能得到答案.因此,这道题可以考虑是否能从左右子树进行递归去解决呢?
首先,要想通过递归来实现,就需要先确定临界条件,那么临界条件是什么呢?换句话说,临界条件就是递归中能够直接返回的特殊情况
    第一点则是最常见的"判空",判断根结点是否是空节点.如果是,那么肯定就可以马上返回了,这是一个临界条件
    再来考虑题意,在以root为根结点的树中找到p结点和q结点的最近公共祖先,那么特殊情况是什么呢?很显然,特殊情况就是根结点就等于q结点或p结点的情况,如果根结点为二者之一,那么根结点就必定是最近公共祖先了,这时直接返回root即可.
    由此看来,这道题就一共有三种特殊情况root==q, root==p和root==null 这三种情况均直接返回root即可
根据临界条件,实际上可以发现这道题已经被简化为查找以root为根结点的树上是否有p结点或者q结点,如果有就返回p结点或q结点,否则返回null

这样一来其实就很简单了:从左右子树分别进行递归,即查找左右子树上是否有p结点或者q结点,就一共有4种情况:
    第一种情况:左子树和右子树均找没有p结点或者q结点;(这里特别需要注意,虽然题目上说了p结点和q结点必定都存在,但是递归的时候必须把所有情况都考虑进去,因为题目给的条件是针对于整棵树,而递归会到局部,不一定都满足整体条件)
    第二种情况:左子树上能找到,但是右子树上找不到,此时就应当直接返回左子树的查找结果
    第三种情况:右子树上能找到,但是左子树上找不到,此时就应当直接返回右子树的查找结果
    第四种情况:左右子树上均能找到,说明此时的p结点和q结点分居root结点两侧,此时就应当直接返回root结点
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if root == p or root == q:
            return root
        # 第四种情况:左右子树都能找到,说明此时的p结点和q结点分居root结点两侧
        if left and right:
            return root
        # 第二种情况:左子树上能找到,但是右子树上找不到,此时就应当直接返回左子树的查找结果
        if left and right==None:
            return left
        # 第三种情况:右子树上能找到,但是左子树上找不到,此时就应当直接返回右子树的查找结果
        if right and left==None:
            return right