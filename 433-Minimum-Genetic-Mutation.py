class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([start])
        visited = set()
        d = 0
        while q:
            N = len(q)
            
            for i in range(N):
                p = q.popleft()
                if p in visited:
                    continue
                visited.add(p)
                if p == end:
                    return d
                #add neighbors
                
                for i in range(len(p)):
                    for c in ['A','C','G','T']:
                        txt = p[:i] + c + p[i+1:]
                        if txt in bank:
                            q.append(txt)
            d += 1
        return -1
                