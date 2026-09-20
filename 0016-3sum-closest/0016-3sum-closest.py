class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest_sum = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) -1 
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total 
                if total == target:
                    return total 
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1
        return closest_sum
     