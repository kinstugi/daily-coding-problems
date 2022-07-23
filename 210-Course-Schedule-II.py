class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visited, cycle = set(), set()
        order = []
        
        def recur(n):
            if n in visited: return True
            if n in cycle:
                return False
            
            cycle.add(n)
            
            for pre in adj[n]:
                if not recur(pre): return False
            
            cycle.remove(n)
            visited.add(n)
            adj[n] = []
            order.append(n)
            return True
        
        for k in adj.keys():
            if not recur(k): return []
        return order