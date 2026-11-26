class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        save =[]

        listed = path.split("/")
        for char in listed: 
            if char == "" or char == ".":
                continue
            elif char == "..":
                if save: 
                    save.pop()
            else:
                save.append(char)
        return "/" + "/".join(save)
            