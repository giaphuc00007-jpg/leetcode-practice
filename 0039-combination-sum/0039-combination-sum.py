class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        result = []
        def backtracking(index,curr_path,curr_sum):
            if  curr_sum == target:
                result.append(list(curr_path))
            if index >= n or curr_sum > target or curr_path in result:
                return 
            
            curr_path.append(candidates[index])
            backtracking(index,curr_path,curr_sum + candidates[index])
            curr_path.pop()

            backtracking(index+1,curr_path,curr_sum)
        backtracking(0,[],0)
        return result