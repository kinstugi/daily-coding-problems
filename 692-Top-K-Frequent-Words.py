from collections import Counter

# i know the you can just sort the hashmap but I was trying to implement bucket sort
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = Counter(words)
        mx = max(mp.values())
        
        array = [[] for _ in range(mx+1)]
        for key,val in mp.items():
            array[val].append(key)
        
        res = []
        for i in range(mx, -1, -1):
            array[i].sort()
            for item in array[i]:
                if k == 0:
                    return res
                res.append(item)
                k -= 1
        return res