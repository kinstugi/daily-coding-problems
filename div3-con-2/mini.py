if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        N = int(input())

        if N < 10:
            print(N)
            continue
        # elif N == 45:
        #     print("123456789")


        arr  = [i for i in range(1, 10, 1)]
        ans = []
        path = []
        
        def canSum(i,tot):
            if tot == 0:
                tmp = path[:]
                tmp.sort()
                res = ""
                for num in tmp:
                    res += f"{num}"
                ans.append(int(res))
                return
            elif tot < 0:
                return
            if i >= len(arr): return
            
            path.append(arr[i])
            canSum(i+1, tot-arr[i])
            path.pop()

            canSum(i+1, tot)
        canSum(0, N)
        print(min(ans))
        
                