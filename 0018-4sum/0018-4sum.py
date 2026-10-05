class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        save = []
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1,len(nums)-2 ):
                if j > i + 1 and nums[j] == nums[j-1]: continue

                right = len(nums) - 1
                left = j + 1 
                while left < right:
                    sum_ = nums[left] + nums[i] + nums[j] + nums[right]
                    if sum_ == target: 
                        save.append([nums[left], nums[i], nums[j], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1 
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                        left += 1 
                    elif sum_ < target:
                        left += 1
                    else: 
                        right -= 1 

        return save 

