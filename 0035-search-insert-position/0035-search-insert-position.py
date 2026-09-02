class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
            return None
        left = 0
        right = len(nums) - 1
        def check(left,right):
            if left > right:
                return left
            mid = (left+right)//2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                return check(left,mid-1)
            elif nums[mid] < target:
                return check(mid+1,right)
            
        return check(left,right)
            
