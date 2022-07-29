from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % (groupSize) != 0: return False
        mp = Counter(hand)
        hand.sort()
        
        g_cnt = groupSize
        i = 0
        while i < len(hand):
            while i < len(hand) and mp[hand[i]] <= 0: # to locate the next group
                i += 1
            if i >= len(hand): break
            st = hand[i] # starting point of group
            for k in range (groupSize):
                if mp.get(st+k, 0) == 0:
                    return False
                mp[st+k] -= 1
    
        
        for v in mp.values():
            if v != 0: return False
        return True