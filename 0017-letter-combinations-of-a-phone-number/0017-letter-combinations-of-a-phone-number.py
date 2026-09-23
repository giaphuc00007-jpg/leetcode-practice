class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        stack = {
            2 : ('a' ,'b','c'),
            3 : ('d','e','f'),
            4 : ('g','h','i'),
            5 : ('j','k','l'),
            6 : ('m','n','o'),
            7 : ('p','q','r','s'),
            8 : ('t','u','v'),
            9 : ('w','x','y','z')
        }
        result = ['']
        for char in digits:
            result = [x+y for x in result for y in stack[int(char)]]        
        return result