from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        Q = deque([root])
        p_mp = {}
        while Q:
            iterLen = len(Q)
            tmp = []
            
            for _ in range(iterLen):
                q = Q.popleft()
                tmp.append(q.val)
                if q.left:
                    Q.append(q.left)
                    p_mp[q.left.val] = q.val
                if q.right:
                    Q.append(q.right)
                    p_mp[q.right.val] = q.val
                
                if x != y and x in tmp and y in tmp and p_mp[x] != p_mp[y]:
                    return True
        return False