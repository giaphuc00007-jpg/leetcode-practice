class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None:
            return None 
        save = {}
        for i in range(len(nums)):
            curr = target - nums[i]
            
            
            if curr in save:
                return [save[curr],i] 
            save[nums[i]]= i

            
               

