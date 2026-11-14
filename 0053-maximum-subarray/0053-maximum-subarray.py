class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tong = 0 
        save = 0 
        start = 0 
        end = 0 
        for i in range(len(nums)):
            tong += nums[i]
            if tong > save:
                save = tong
            if tong < 0:
                tong = 0 
        if max(nums) < 0: 
            return max(nums)
        return save


