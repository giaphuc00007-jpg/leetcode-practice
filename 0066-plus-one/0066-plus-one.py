class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None:
            return None
        so = -1 
        digits[so] += 1
        while digits[so] > 9:
            digits[so] = 0
            so -= 1 
            
            if abs(so) >len(digits):
                digits.insert(0, 1)
                break
            digits[so] += 1
        return digits
