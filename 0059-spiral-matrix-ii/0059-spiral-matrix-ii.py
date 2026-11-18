class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        save = [[0] * n for _ in range(n)]

        top,left = 0,0 
        bot,right = n-1 ,n -1
        num = 1
        while top <= bot or left <= right:
            for i in range(left,right+1):
                save[top][i] = num
                num += 1
            top += 1
            for i in range(top,bot+1):
                save[i][right] = num
                num += 1
            right -= 1 
            if bot >= top:
                for i in range(right,left-1,-1):
                    save[bot][i] = num
                    num += 1 
                bot -= 1
            if right >= left:
                for i in range(bot,top-1,-1):
                    save[i][left] = num
                    num += 1 
                left += 1 
        return save


            