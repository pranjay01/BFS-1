# Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity -> On since we are iteating over each element and prossesing it's child ones
# Space complexity -> the length of queue
# Logic - > for each level found all the child at low level and add in the result lest then process all items of that level and continue


from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        levelQueue = deque()

        if root!=None:
            levelQueue.append(root)

        while len(levelQueue) > 0:
            internalList = []
            itemsInCurrentLevel = len(levelQueue)
            for i in range(itemsInCurrentLevel):
                node = levelQueue.popleft()
                internalList.append(node.val)
                if node.left != None:
                    levelQueue.append(node.left)
                if node.right != None:
                    levelQueue.append(node.right)
            result.append(internalList)

        return result