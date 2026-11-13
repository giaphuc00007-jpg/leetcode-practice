class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    
        save = []
        result =[]
        for c in strs:
            s = sorted(c)
            if s not in save:
                save.append(s)
                result.append([])
            if s in save:
                vi_tri = save.index(s)
                result[vi_tri].append(c)
        return result

