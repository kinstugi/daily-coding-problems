from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        lvl = 0
        Q = deque([root])
        
        def validate(lvl, arr, val):
            if lvl % 2 == 0:
                if val % 2 == 0: return False
                if not arr: return True
                if arr[-1] >= val: return False
            else:
                if val % 2 == 1: return False
                if not arr: return True
                if arr[-1] <= val: return False
            return True
        
        while Q:
            N = len(Q)
            tmp = []
            for _ in range(N):
                node = Q.popleft()
                if not validate(lvl, tmp, node.val): return False
                tmp.append(node.val)
                
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
            lvl += 1
        return True