class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        elif haystack is None and needle is None:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i 

                