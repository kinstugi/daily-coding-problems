from bisect import bisect_right
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r = matrix[0][0], matrix[-1][-1]
        N = len(matrix)
        
        def less_k(num):
            cnt = 0
            for r in range(N):
                x = bisect_right(matrix[r], num)
                cnt += x
            return cnt
        
        while l < r:
            mid = l + (r-l)//2
            cnt = less_k(mid)
            
            if cnt < k:
                l = mid + 1
            else:
                r = mid
        return l