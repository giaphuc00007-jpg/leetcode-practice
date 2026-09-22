class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        stack = {
            1000 : 'M',
            500 : 'D',
            100 : 'C',
            50 : 'L',
            10 : 'X',
            5 : 'V',
            1 : 'I'
        }
        keys = sorted(stack.keys(), reverse=True)
        while num >= 1000:
            num -= 1000
            result += stack[keys[0]]
        
        for i in range(len(keys)):
            so_lon = keys[i]
            
            while num >= so_lon:
                num -= so_lon
                result += stack[so_lon]


            if i %2 ==0 and i+2 < len(keys):
                save_9 = so_lon - keys[i+2]
                if num >= save_9:
                    num -= save_9
                    result += stack[keys[i+2]] + stack[so_lon]

                    
            if i %2 == 1 and i + 1 < len(keys):
                so_nho = keys[i+1]
                save_4 = so_lon - so_nho
                if num >= save_4:
                    num -= save_4
                    result += stack[so_nho] + stack[so_lon]
            
        return result
                