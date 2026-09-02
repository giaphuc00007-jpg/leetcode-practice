# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        stack = []
        def check(node):
            if node is None:
                return None
             
            check(node.left) 
            stack.append(node.val)
            check(node.right)

        check(root) 
        return stack
