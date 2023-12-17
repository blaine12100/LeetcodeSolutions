"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
leaf node.

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Solution 1: Use recursion solution where we call recursively for left subtree and right subtree. When root is none,
return 0. The overall solution is: max(height of left subtree, height of right subtree) + 1
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            lh = self.maxDepth(root.left)
            rh = self.maxDepth(root.right)
            return max(lh, rh) + 1
