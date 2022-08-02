if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, H, M = map(int, input().strip().split())

        #earliest time he will be awoken
        tot_min = (H * 60) + M
        ans = float('inf')

        for _ in range(n):
            h,m = map(int, input().strip().split())

            alarm_min = (h * 60) + m
            if alarm_min < tot_min:
                alarm_min += 1440
            ans = min(alarm_min- tot_min, ans)
        
        print(ans//60, ans % 60)
            



            


