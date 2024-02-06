# # 1. 문자열의 회문 검사
# arr = 'abcdedcba'
# M = len(arr)
# s = 0
# e = M - 1
# possible = True
# for i in range(M//2):
#     # arr[s+i] != arr[e-i]
#     if arr[s+i] != arr[e-i]:
#         possible = False
#         break
# print(possible )
#
# # 2. 길이 N인 문자열 내에 모든 가능한 문자열 조사
# N = 8
# M = 4
# arr = 'cbbcbaab'
# print(arr)
# for s in range(N-M+1):
#     e = s + M - 1
#     for i in range(M//2):
#         if arr[s+i] != arr[e-i]:
#             break
#     else:
#         print(arr[s: s + M])

# 3. 모든 행에 대해 적용
# 가장 긴 회문의 길이를 구하는 문제

T = 10
for tc in range(1, T+1):
    M = 8
    L = int(input())
    arr = [input() for _ in range(M)]
    cnt = 0

    # 가로
    for r in range(M):
        for c in range(M - L + 1): # 시작점
            e = c + L - 1  # 끝점
            for i in range(L//2):
                if arr[r][c + i] != arr[r][e - i]:
                    break
            else:
                cnt += 1
    # 세로
    for c in range(M):
        for k in range(M - L + 1):
            tmpStr = ""
            for r in range(k, k+L):
                tmpStr += arr[r][c]
            for t in range(L//2):
                if tmpStr[t] != tmpStr[L - t - 1]:
                    break
            else:
                cnt += 1
    print(f'#{tc } {cnt}')






