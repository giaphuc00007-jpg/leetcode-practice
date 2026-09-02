class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        save = []
        for char in range(len(s)):
            if s[char] not in stack:
                if save and s[char] == save[-1] :
                    save.pop()
                else:
                    return False

            if s[char] in stack:
                save.append(stack[s[char]])
        return len(save) == 0
        
