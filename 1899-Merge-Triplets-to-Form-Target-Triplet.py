class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    
        mx_a = mx_b = mx_c = 0
        for a,b,c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                mx_a = max(a, mx_a)
                mx_b = max(b, mx_b)
                mx_c = max(c, mx_c)
    
        return [mx_a, mx_b, mx_c] == target
        