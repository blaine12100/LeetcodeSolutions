"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
level by level).

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Solution 1: The solution needs to be iterative as we need to return values / print them. If we try a recursive solution,
we cannot switch between left and right subtrees of a given node.

Queue data-structure needs to be used for this.

Step 1: Add root node to queue
Add children of current node to the end of queue. Once children are added, remove current node from queue as
it's processing has been done. The same logic can be applied to Nth tree level order traversal.

The code terminates when there are no more children left to be processed.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # This is either pre or post order
        # Check if node is leaf node:
        # print(root.val)
        if root:
            '''if  root.left == None and root.right == None:
                print(root.val)
                return
            else:
                print(root.val)
                if root.left!=None:    
                    self.levelOrder(root.left)
                if root.right!=None:
                    self.levelOrder(root.right)'''
            # if current_element.left!=None and current_element.right!=None:
            #   level_order.append([current_element.left.val, current_element.right.val])
            # elif current_element.left!=None:
            #    level_order.append([current_element.left.val])
            # elif current_element.right!=None:
            #    level_order.append([current_element.right.val])
            # print(temp_queue)
            temp_queue = [root]
            level_order = [[root.val]]

            # Op /s partially correct. Need to introduce some concept of level using which successive level arrays
            # can be merged.
            while temp_queue:
                current_element = temp_queue.pop(0)
                # print(current_element.val)
                if current_element.left != None:
                    temp_queue.append(current_element.left)
                if current_element.right != None:
                    temp_queue.append(current_element.right)
                # print(temp_queue)
                # temp_queue.pop(0)
                level_order.append([x.val for x in temp_queue])
            print(level_order)
            return level_order
        else:
            return []
