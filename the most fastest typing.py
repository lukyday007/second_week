T = int(input())
for tc in range(1, T+1):
    aaa, ta = map(str, input().split())

    cnt = len(aaa)
    for i in range(len(aaa) - len(ta) + 1):
        if aaa[i:i+len(ta)] == ta:
            cnt -= (len(ta)-1)
    print(f"#{tc} {cnt}")
