# # ver 1: GNS
# digitDict = {'ZRO': 0,'ONE': 1,'TWO': 2,'THR': 3,'FOR': 4,'FIV': 5,'SIX': 6, 'SVN': 7,'EGT': 8,'NIN': 9}
#
# T = int(input())
# for tc in range(1, T+1):
#     digit = [0] * 10
#     N = int(input())
#     other = list(map(str, input().split()))
#
#     for o in other:
#         digit[digitDict[o]] += 1
#
#     print(f"#{tc}", end=" ")
#     for k, v in digitDict.items():
#         for _ in range(digit[v]):
#             print(k, end=" ")
#
#     print()

# ver 수정
digitDict = {'ZRO': 0,'ONE': 1,'TWO': 2,'THR': 3,'FOR': 4,'FIV': 5,'SIX': 6, 'SVN': 7,'EGT': 8,'NIN': 9}

T = int(input())
for tc in range(1, T+1):
    digit = [0] * 10
    test , N = input().split()
    other = list(map(str, input().split()))

    for o in other:
        digit[digitDict[o]] += 1

    print(f"#{tc}") # 밑에 end=" "이 있어서 두번 쓸 필요가 없었음
    for k, v in digitDict.items():
        for _ in range(digit[v]):
            print(k, end=" ")

# Ver 3 : 메모리 적게 쓰는 방법
T = int(input())
for tc in range(1, T + 1):
    case, N = input().split()
    arr = list(input().split())

    lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    num = []
    for i in lst:
        cnt = arr.count(i)
        num.append(cnt)

    print(f'#{tc}')
    for j in range(10):
        print((lst[j] + ' ') * num[j], end='')