# 문자열_회문_확인용
row, col = 10, 10
'''
1
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
'''
# ver 1
T = int(input())
for tc in range(1, T+1):
    row, length = map(int, input().split())
    lst = [input() for _ in range(row)]
    arr = []
    ans = ""
    # 가로열
    for r in range(row):
        for c in range(row - length + 1):
            tmpStr = lst[r][c: c + length]
            arr.append(tmpStr)
    # 세로열
    for c in range(row):
        tmpStr = ""
        for r in range(row - length + 1):
            for k in range(r, r+length):
                tmpStr += lst[k][c]
        arr.append(tmpStr)

    for a in arr:
        aList = list(a)
        check = True
        while len(aList) > 0:
            if len(aList) == 1:
                break
            if aList.pop(0) == aList.pop():
                check = True
            else:
                check = False
                break

        if check == True:
            ans = a
            break

    print(f"#{tc} {ans}")

# ver 2
T = int(input())
for tc in range(1, T + 1):
    row, length = map(int, input().split())
    lst = [input() for _ in range(row)]
    arr = []
    ans = ""
    # 가로열
    for r in range(row):
        for c in range(row - length + 1):
            tmpStr = lst[r][c: c + length]
            arr.append(tmpStr)
    # 세로열
    for c in range(row):
        for r in range(row - length + 1):
            tmpStr = ""
            for k in range(r, r + length):
                tmpStr += lst[k][c]
            arr.append(tmpStr)

    for a in arr:
        aList = list(a)
        check = True
        while len(aList) > 0:
            if len(aList) == 1:
                break
            if aList.pop(0) == aList.pop():
                check = True
            else:
                check = False
                break

        if check == True:
            ans = a
            break

    print(f"#{tc} {ans}")











