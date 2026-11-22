class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        duong_phai_di = m + n -2 
        di_doc = m -1 
        di_ngang = n - 1 

        hv_dg_ph_di = 1 
        for i in range(1,duong_phai_di + 1 ):
            hv_dg_ph_di *= i 
        hv_doc = 1
        for i in range(1,di_doc + 1 ):
            hv_doc *= i 
        hv_ngang = 1 
        for i in range(1,di_ngang + 1 ):
            hv_ngang *= i 
        return hv_dg_ph_di / (hv_doc*hv_ngang)
