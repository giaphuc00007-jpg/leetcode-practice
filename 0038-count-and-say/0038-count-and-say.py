class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = "1"
 
        for _ in range(n-1):
            count = 1
            stack = []
            for i in range(len(nums)):
                num = nums[i]
                if i+1 < len(nums) and num == nums[i+1] :
                    count += 1
                if i+1 == len(nums) or num != nums[i+1]:
                    stack.append(str(count)+num)
                    count = 1
            nums="".join(stack)
        return nums
                