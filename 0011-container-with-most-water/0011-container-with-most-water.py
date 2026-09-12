class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
         
        right = len(height) -1
        left = 0 
        result = 0 
        while left < right:
        
            current = min(height[left],height[right]) * (right - left)
            result = max(result, current)
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1
        return result 