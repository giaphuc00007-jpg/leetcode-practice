class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtracking(answer, count_open, count_close):
            if len(answer) == 2*n:
                result.append(answer)
                return
            if count_open < n:
                backtracking(answer + '(', count_open + 1, count_close)
            if count_close < count_open:
                backtracking(answer + ')', count_open, count_close + 1)
        backtracking("",0,0)
        return result
  

            