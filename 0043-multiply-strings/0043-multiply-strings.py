class Solution(object):
    def multiply(self, num1, num2):
        if num1  == "0" or num2 == "0":
            return "0"
        dictionnary_num = {
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7': 7,
            '8' : 8,
            '9' :9,
            '0' : 0 
            }
            
        dictionnary_str = {
            1 : '1',
            2 : '2',
            3 : '3',
            4 : '4',
            5 : '5',
            6 : '6',
            7 : '7',
            8 : '8',
            9 : '9',
            0 : '0'
            }
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                p1 = i+j
                p2 = i + j + 1 
                d1 = dictionnary_num[num1[i]]
                d2 = dictionnary_num[num2[j]]
                total =  d1 * d2 + result[p2]
                result[p2] = total %10
                result[p1] += total // 10
        idx = 0
        while idx < len(result) and result[idx] == 0:
            idx += 1
        return "".join(dictionnary_str[digit] for digit in result[idx:])

