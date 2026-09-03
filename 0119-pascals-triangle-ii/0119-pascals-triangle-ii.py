class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        stack=[]
        for i in range(rowIndex+1):
            
            save = [1]*(i+1)
            if i >= 2:
                for n in range(1,i):
                    save[n] = stack[i-1][n] + stack[i-1][n-1] 

            stack.append(save)
        return stack[rowIndex]