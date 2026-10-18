class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """ 
        count = 0
        phan_tu = 0 
        
        so_bi_chia = abs(dividend)
        so_chia = abs(divisor)

        while so_bi_chia >= so_chia: 
            so_tru = so_chia << phan_tu
            while so_tru <= so_bi_chia:
                phan_tu += 1
                so_tru = so_chia << phan_tu
            
            so_bi_chia -= (so_chia << (phan_tu - 1))
            count += (1<<(phan_tu-1))
            phan_tu = 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend< 0 and  divisor <0:
            return count 
        elif dividend< 0 or divisor <0: 
            return -count 
        if count >= 2**31 -1:
            return 2**31 -1
        elif count <= -2**31:
            return -2**31
        return count 
            

