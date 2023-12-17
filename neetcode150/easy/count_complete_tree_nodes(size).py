"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Solution 1: Use a traversal algorithm (Level Order, pre,post,in) to visit the nodes and each time a node is visited,
increment the count of visited nodes. This can be either done by using an object variable or it can be done by the recur
sive counting method.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    current_size = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Solution 1
        """if root:
            self.current_size+=1
            if root.left!=None:
                self.countNodes(root.left)
            if root.right!=None:
                self.countNodes(root.right)
            if root.left == None and root.right == None:
                return 1
        return self.current_size"""

        # Solution 2 (Slightly slower than solution 1)
        '''if root == None:
            return 0
        else:
            left = self.countNodes(root.left)
            right = self.countNodes(root.right)
            return left + right + 1'''
