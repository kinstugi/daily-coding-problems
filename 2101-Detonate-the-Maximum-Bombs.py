class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # it lies in center if distance between centers is less than  or equal to radius
        def get_distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return ((x1-x2)**2  + (y1 - y2)**2) ** 0.5
        
        adj = defaultdict(list)
        
        for i in range(len(bombs)):
            x1,y1, r1 = bombs[i]
            
            for j in range(len(bombs)):
                x2,y2, r2 = bombs[j]
                if i == j: continue
                d = get_distance((x1,y1), (x2,y2))
                
                if r1 >= d:
                    adj[i].append(j)
                    adj[j]
        
        
        def dfs(n, seen):
            if n in seen: return 0
            seen.add(n)
            res = 1
            for nei in adj[n]:
                res += dfs(nei, seen)
            return res
        
        mx = 1
        for k in adj.keys():
            d = dfs(k, set())
            mx = max(mx, d)
        return mx