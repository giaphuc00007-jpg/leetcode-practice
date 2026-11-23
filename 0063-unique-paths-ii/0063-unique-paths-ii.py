class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if  obstacleGrid[-1][-1] == 1:
            return 0 
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for row in obstacleGrid:
            row.append(0)
        obstacleGrid.append([0] * (n + 1))
        
        obstacleGrid[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    continue 
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue 
                right = obstacleGrid[i][j+1]
                down = obstacleGrid[i+1][j]
                obstacleGrid[i][j] = right +down 
        return obstacleGrid[0][0]
                
