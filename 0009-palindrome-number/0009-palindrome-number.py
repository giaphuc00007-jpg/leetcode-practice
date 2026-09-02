class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        curr = str(x)
        if curr == curr[::-1]:
            return True
        else: return False