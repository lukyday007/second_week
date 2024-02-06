def check(L, arr):
    for r in range(100):
        for c in range(100 - L + 1): # 시작점
            e = c + L - 1  # 끝점
            possible = False
            for i in range(L//2):
                if arr[r][c + i] != arr[r][e - i]:
                    break
            else:
                return L

    # 세로
    for c in range(100):
        for k in range(100 - L + 1):
            tmpStr = ""
            for r in range(k, k+L):
                tmpStr += arr[r][c]
            for t in range(L//2):
                if tmpStr[t] != tmpStr[L - t - 1]:
                    break
            else:
                return L

    return 0

T = 10
for tc in range(1, T+1):
    L = int(input())
    arr = [input() for _ in range(100)]
    cnt = 0

    for i in range(100, 0, -1):
        result = check(i, arr)
        if result:
            break

    print(f'#{tc } {result}')