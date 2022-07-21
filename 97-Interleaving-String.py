class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def recur(i,j):
            if (i,j) in memo: return memo[(i,j)]
            if i == len(s1) and j == len(s2):
                return (i+j) == len(s3)
            
            res = False
            if i < len(s1):
                if (i+j) < len(s3) and s3[i+j] == s1[i]:
                    res = res or recur(i+1, j)
            
            if j < len(s2):
                if (i+j) < len(s3) and s3[i+j] == s2[j]:   
                    res = res or recur(i, j+1)
            memo[(i,j)] = res
            return res
        return recur(0,0)