class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(curr_save, result,nums):
            if len(curr_save) == len(nums):
                result.append(curr_save[:])
                return 
            for num in nums:
                if num in curr_save: continue
                curr_save.append(num)
                backtracking(curr_save, result,nums)
                curr_save.pop()
        result = []
        backtracking([],result,nums)
        return result
