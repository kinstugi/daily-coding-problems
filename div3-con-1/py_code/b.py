if __name__ == '__main__':
    N = int(input())
    txt = input()

    mp = {}
    mx = 0
    for i in range(1, N):
        key = txt[i-1] + txt[i]
        mp[key] = mp.get(key, 0) + 1
        mx = max(mx, mp[key])
    
    for k,v in mp.items():
        if v == mx:
            print(k)
            break
    

