# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        def depth(node):
            if node is None:
                return 0
            return 1+max(depth(node.left),depth(node.right))
         
        return abs(depth(root.left)-depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
         