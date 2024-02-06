# ppt 코드
# p = 'is'  # 찾을 패턴
# t = 'This is a book'
# M = len(p)
# N = len(t)
#
# def BruteForce(p, t):
#     i = 0
#     j = 0
#     while j < M and i < N:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#
#     if j == M: return i - M
#     else: return -1

# # 문제 예시 코드
# def f(pat, txt, M, N):
#     for i in range(N - M + 1):
#         for j in range(M):
#             if txt[i + j] != pat[j]:
#                 break
#         else:
#             return 1
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     pat = input()
#     txt = input()
#     M = len(pat)
#     N = len(txt)

# KMP
# def kmp(t, p):
#     N = len(t)
#     M = len(p)
#     lps = [0] * (M + 1)
#     # preprocessing
#     j = 0   # 일치한 개수 == 비교할 패턴 위치
#     lps[0] = -1
#     for i in range(1, M):
#         lps[i] = j  # p[i] 이전에 일치한 개수
#         if p[i] == p[j]:
#             j += 1
#         else:
#             j = 0
#     lps[M] = j
#     # search
#     i = 0   # 비교할 텍스트 위치
#     j = 0   # 비교할 패턴 위치
#     while i < N and j <= M:
#         if j == -1 or t[i] == p[j]:  # 첫글자가 불일치했건, 일치하면
#             i += 1  # i는 다음 위치로
#             j += 1  # j는 0으로
#         else:   # 불일치
#             j = lps[j]
#
#         if j == M:  # 패턴을 찾을 경우
#             print(i - M, end=' ')   # 패턴의 인덱스 출력
#             j = lps[j]
#
#     print()
#     return
#
# t = 'zzzabcdabcdabcefabcd'
# p = 'abcdabcef'
# kmp(t, p)
# t = 'AABAACAADAABAABA'
# p = 'AABA'
# kmp(t, p)


# # 패턴 매칭 : 패턴이 매칭되는 모든 경우를 찾는다
# # 염기서열 (ACTG 네개의 물질)
# p = "CATTCCCTGCGCCGC"                                                                       # pattern
# t = "ATTTGTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text
# # 구간합 문제와 유사
# # 패턴이 존재할 수 있는 모든 '시작 위치'
# N, M = len(t), len(p)
# for s in range(0, N-M + 1):
#     # text의 s에서 s + M - 1
#     # 패턴의 길이만큼 비교
#     found = True    # break 가 잘 걸렸는지 체크
#     for i in range(M):  # 0 - M-1
#         if t[s+i] != p[i]:  # 같으면 뒤로 뒤로 계속 비교, 그러니 같지 않을 때를 처리
#             found = False
#             break
#     if found:
#         print(s, t[s:s + M])


# brute-force 매칭
def check_matching(string, txt):
    for t in range(len(text)-len(check)+1):
        for c in range(len(check)):
            if text[t + c] !=  check[c]:
                break
        else:
            return 1
    return 0
T = int(input())
for tc in range(1, T+1):
    check = input()
    text = input()
    result = check_matching(check, text)
    print(f"#{tc} {result}")








































