# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(left,right):
            if left is None and right is None:
                return True
            elif left is None and right is not None:
                return False 
            elif left is not None and right is None:
                return False 
            elif left.val != right.val:
                return False
            else:
                return check(left.left,right.right) and check(left.right,right.left)
        return check(root.left,root.right)
