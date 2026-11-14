class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        best = nums[0]
        for x in nums[1:]:
            current = max(x, current+x)
            best = max(current,best)
        return best