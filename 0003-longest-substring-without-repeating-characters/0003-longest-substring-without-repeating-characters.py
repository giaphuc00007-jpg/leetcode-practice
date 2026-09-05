class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        strs = ""
        max_len = 0 
        for char in s:
            if char in strs:
                index = strs.index(char)
                strs = strs[index+1:]

            strs += char
            max_len = max(max_len,len(strs))
        return max_len

            