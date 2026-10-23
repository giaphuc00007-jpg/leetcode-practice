class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = []
        col = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue 
                if val in row:
                    return False 
                row.append(val)
                
            row = []
            for k in range(9):
                val = board[k][i]
                if val == ".":
                    continue 
                if val in col:
                    return False 
                col.append(val)
                
            col =[]
        box = []
        start_c = 0 
        end_c = 3
        

        start_r = 0 
        end_r = 3
        
        for i in range(9):
            for r in range(start_r,end_r):
                for c in range(start_c,end_c):
                    val = board[r][c]
                    if val == ".":
                        continue
                    if val in box:
                        return False
                    box.append(val) 
            box =[]
            start_c = end_c 
            end_c += 3
            if start_c >= 9:
                start_c = 0 
                end_c = 3
                
                start_r = end_r
                end_r += 3

        return True

