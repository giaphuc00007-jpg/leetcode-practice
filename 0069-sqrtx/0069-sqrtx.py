class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None 
        def check(left,right):
            if left > right:
                return right
            mid = (left + right) /2 
            if mid*mid == x:
                return mid 
            elif mid*mid > x:
                return check(left, mid-1)
            elif mid*mid < x:
                return check(mid+1,right)
        return check(0,x)