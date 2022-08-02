if __name__ == '__main__':
    t = int(input())

    for  _ in range(t):
        N = int(input())
        arr = list(map(int, input().strip().split()))

        seen = set()
        cnt = 0
        for i in range(N-1, -1, -1):
            if arr[i] in seen:
                break
            seen.add(arr[i])
            cnt += 1
        
        print(N - cnt)
        