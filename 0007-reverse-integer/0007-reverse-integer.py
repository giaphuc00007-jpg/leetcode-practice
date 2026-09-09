class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) < 10:
            return x
        luu = 1 
        if x < 0:
            luu = -1 
        start = abs(x)
        result = 0
        so = len(str(start)) - 1 
        ti_so = pow(10,so)
        while start > 0:
            doi_nguoc = start % 10 
            start = start // 10 

            result = result + ti_so * doi_nguoc
            
            ti_so = ti_so // 10 
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result*luu
 