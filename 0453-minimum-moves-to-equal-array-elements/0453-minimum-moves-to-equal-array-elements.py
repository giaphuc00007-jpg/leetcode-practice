class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        min_num = nums[0]
        n = len(nums) -1 
        tong = 0
        for char in nums:
            tong += ( min_num - char) 
        return tong / (n-len(nums))