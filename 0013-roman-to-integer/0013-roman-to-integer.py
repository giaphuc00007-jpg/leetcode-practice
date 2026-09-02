class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        save = {
            'I' :  1,
            'V' :  5,
            'X' :  10,
            'L' :  50,
            'C' :  100,
            'D' :  500,
            'M' :  1000
        }
        old = 0
        total = 0
        for i in range(len(s)):
            curr = save[s[i]]
            if curr>old:
                total += curr - 2 * old 

            else:
                total += curr
            
            old = curr
        return total


            