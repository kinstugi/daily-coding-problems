class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = -1
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                l = i
        
        if l == -1: return ""
        return num[:l+1]
        