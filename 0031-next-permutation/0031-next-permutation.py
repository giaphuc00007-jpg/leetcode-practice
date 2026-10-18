class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sort = sorted(nums)
        dap_an =sort[::-1]
        if nums == dap_an :
            return nums.reverse()
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                vi_tri = i - 1
                tro = len(nums) - 1
                while nums[tro] <= nums[vi_tri]:
                    tro -= 1 
    
                temp = nums[vi_tri] 
                nums[vi_tri] =nums[tro]
                nums[tro] = temp
                
                nums[vi_tri+1:] = sorted(nums[vi_tri+1:])
                break
        
        return nums 



