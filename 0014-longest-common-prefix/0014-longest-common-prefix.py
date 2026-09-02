class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        news = sorted(strs)
        first = news[0]
        last = news[-1]
        result = ""
        for char in range(len(first)):
            if first[char] == last[char]:
                result= result + first[char]
            else: break
        return result



