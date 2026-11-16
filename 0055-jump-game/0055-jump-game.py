class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        now = 0 
        while now < n -1:
            step = nums[now]
            best_vt = now
            max = 0
            for i in range(1,step +1):
                vi_tri = now + i
                
                if vi_tri < n:
                    tong = vi_tri + nums[vi_tri]
                
                if tong > max:
                    max = tong 
                    best_vt = vi_tri
            now = best_vt
            if step == 0 and now < n-1:
                return False
        return True
            
        