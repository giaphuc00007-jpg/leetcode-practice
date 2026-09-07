class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            left = i
            right = i 
            while left >= 0 and right < len(s)  and s[left] == s[right]:
                left -= 1 
                right += 1
            
            left2 = i
            right2 = i +1
            while left2 >= 0 and right2 < len(s)  and s[left2] == s[right2]:
                left2 -= 1 
                right2 += 1
            
            s1 = s[left+1:right]
            s2 = s[left2+1:right2]

            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res

