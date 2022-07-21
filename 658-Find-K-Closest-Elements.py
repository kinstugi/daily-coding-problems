class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        
        for num in arr:
            d = abs(x-num)
            heapq.heappush(maxHeap,(-d, -num))
            
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        ans = [-v for k,v in maxHeap]
        ans.sort()
        return ans