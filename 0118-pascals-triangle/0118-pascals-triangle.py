class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        stack = []
        for i in range(1,numRows+1):
            item = [1]*i
            if i > 2:
                for n in range(1,i-1):
                    item[n] = stack[i-2][n] + stack[i-2][n-1]
                 
            stack.append(item)
        return stack
