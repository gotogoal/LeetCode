#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :       2022/10/31 20:29
# @Author   :       YH
# @FILE     :       236_LowestCommonAncestor.py
# @Software :       PyCharm


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
        if left and right:
            return root
        if left and right==None:
            return left
        if right and left==None:
            return right