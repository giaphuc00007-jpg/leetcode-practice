class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
        n = len(nums)
        if n <= 1:
            return 0 
        now = 0 
        while now < n-1: 
            step = nums[now]
            if now+ step >= n -1 :
                return count + 1 
            max = 0 
            best = now
            for i in range(1,step + 1 ):
                vi_tri = now + i
                tong = vi_tri + nums[vi_tri]
                if tong > max: 
                    max = tong 
                    best = vi_tri 
            now = best 
            count += 1
        return count 
