class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = {}
        for i, ls in enumerate(list1):
            mp[ls] = i
        
        minHeap = []
        mn = float('inf')
        for i, ls in enumerate(list2):
            if ls in mp:
                minHeap.append((i + mp[ls], ls))
                mn = min(mn, i + mp[ls])
        
        return [b for a,b in minHeap if a == mn]