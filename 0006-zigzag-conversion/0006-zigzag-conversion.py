class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        current_row = 0 
        row = [''] * numRows
        goingup = False 
        
        for char in s:
            row[current_row]+=(char)

            if current_row == numRows - 1:
                goingup = True
            elif current_row == 0:
                goingup = False
            current_row += 1 if not goingup else -1 
        return "".join(row)
            
